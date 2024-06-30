# Copyright (c) 2022 Moritz E. Beber
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Test the cookiecutter template initialization."""

from __future__ import annotations

import datetime
import os
import subprocess
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter
from git import Repo


TEMPLATE = Path(__file__).parents[1]


@pytest.fixture(scope="module", params=["GitHub", "GitLab"])
def dev_platform(request: pytest.FixtureRequest) -> str:
    """Provide a recognized development platform."""
    return request.param


@pytest.fixture(
    scope="module",
    params=["MIT", "BSD-3-Clause", "Apache-2.0", "LicenseRef-Proprietary"],
)
def license(request: pytest.FixtureRequest) -> str:
    """Provide a recognized license classification."""
    return request.param


@pytest.fixture()
def cookie_path(
    tmp_path_factory: pytest.TempPathFactory,
    dev_platform: str,
    license: str,
) -> Path:
    """Provide a cookiecutter working directory."""
    return tmp_path_factory.mktemp("cookie") / dev_platform / license


@pytest.fixture(scope="module")
def cookie_context() -> dict[str, str]:
    """Provide a full project context."""
    today = datetime.datetime.now(tz=datetime.timezone.utc).date()
    return {
        "full_name": "Rick Sanchez",
        "email": "rick@galaxybrain.science",
        "dev_platform_username": "rickprime",
        "project_name": "Alien Clones",
        "project_slug": "alien-clones",
        "project_module": "alien_clones",
        "project_short_description": "Wubba Lubba Dub-Dub",
        "release_date": str(today),
        "year": str(today.year),
    }


def test_init_template(
    cookie_path: Path,
    cookie_context: dict[str, str],
    dev_platform: str,
    license: str,
) -> None:
    """Expect that the template can be initialized with any provided license."""
    cookiecutter(
        template=str(TEMPLATE),
        no_input=True,
        output_dir=cookie_path,
        extra_context={
            **cookie_context,
            "dev_platform": dev_platform,
            "license": license,
        },
    )
    project_files = {path.relative_to(cookie_path) for path in cookie_path.rglob("*")}
    expected = {
        Path("alien-clones"),
        Path("alien-clones") / "README.md",
        Path("alien-clones") / "pyproject.toml",
        Path("alien-clones") / "src",
        Path("alien-clones") / "tests",
    }
    assert expected.issubset(project_files), expected.difference(project_files)
    if license != "LicenseRef-Proprietary":
        assert Path("alien-clones") / "LICENSE" in project_files


def test_init_template_tests(cookie_path: Path, cookie_context: dict[str, str]) -> None:
    """Expect that the test suite passes for the initialized template."""
    cookiecutter(
        template=str(TEMPLATE),
        no_input=True,
        output_dir=cookie_path,
        extra_context={
            **cookie_context,
            "dev_platform": "GitHub",
            "license": "MIT",
        },
    )
    project_dir = (cookie_path / cookie_context["project_slug"]).resolve(strict=True)

    # Initialize a git repository such that hatch-vcs can be used.
    repo = Repo.init(project_dir)
    repo.index.add(
        [
            Path(dirpath, name)
            for dirpath, _, filenames in os.walk(project_dir)
            for name in filenames
        ],
    )
    repo.index.commit("chore: initialize cookiecutter template")

    # Run the local test suite.
    try:
        subprocess.run(
            ["hatch", "run", "install:check"],
            cwd=project_dir,
            check=True,
            capture_output=True,
            shell=True,
        )
        subprocess.run(
            ["hatch", "run", "test:run"],
            cwd=project_dir,
            check=True,
            capture_output=True,
            shell=True,
        )
        subprocess.run(
            ["hatch", "run", "docs:build"],
            cwd=project_dir,
            check=True,
            capture_output=True,
            shell=True,
        )
        subprocess.run(
            ["hatch", "run", "style:check"],
            cwd=project_dir,
            check=True,
            capture_output=True,
            shell=True,
        )
    except subprocess.CalledProcessError as error:
        print(error.stdout.decode())  # noqa: T201
        print(error.stderr.decode())  # noqa: T201
        raise
