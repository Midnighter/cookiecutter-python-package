#!/usr/bin/env python
# Copyright (c) 2023 Moritz E. Beber
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


"""Perform post-project generation clean up tasks."""


import logging
import shutil
from pathlib import Path


logger = logging.getLogger(__name__)


def remove_github() -> None:
    """Remove files and directories only required for GitHub."""
    remove = [Path(".github")]
    for path in remove:
        if path.is_dir():
            logger.debug("Cleaning up directory '%s'.", str(path))
            shutil.rmtree(path)


if __name__ == "__main__":
    logging.basicConfig(level="INFO", format="[%(levelname)s] %(message)s")
    if "{{ cookiecutter.dev_platform }}" == "GitLab":
        remove_github()
