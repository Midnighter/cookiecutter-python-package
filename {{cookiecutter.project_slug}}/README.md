# {{cookiecutter.project_name}}

| |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg)](https://pypi.org/project/{{cookiecutter.project_slug}}/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}}.svg)](https://pypi.org/project/{{cookiecutter.project_slug}}/) [![Documentation](https://readthedocs.org/projects/{{cookiecutter.project_slug}}/badge/?version=latest)](https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/?badge=latest)                                                                                                                                                                         |
| Meta | [![{{ cookiecutter.license }}](https://img.shields.io/pypi/l/{{cookiecutter.project_slug}}.svg)](LICENSE) [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](.github/CODE_OF_CONDUCT.md) [![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)                                                                                                                                                          |
| Automation | [![GitHub Workflow]({{ cookiecutter.__dev_platform_url }}/{{cookiecutter.dev_platform_username}}/{{cookiecutter.project_slug}}/workflows/CI-CD/badge.svg)]({{ cookiecutter.__dev_platform_url }}/{{cookiecutter.dev_platform_username}}/{{cookiecutter.project_slug}}/workflows/CI-CD) [![Code Coverage](https://codecov.io/gh/{{cookiecutter.dev_platform_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.dev_platform_username}}/{{cookiecutter.project_slug}}) |

{{cookiecutter.project_short_description}}

## Post Template-Instantiation Steps

1. Start working with git.

    ```shell
    git init
    ```

2. Commit all the files.

    ```shell
    git add .
    git commit -m "chore: initialize project cookiecutter"
    ```

3. Create a repository on `GitHub <https://github.com/>`_ if you haven't done
   so yet.
4. Browse through the architecture decision records (``docs/adr``) if you want
   to understand details of the package design.
5. Remove this section from the readme and describe what your package is all
   about.
6. When you're ready to make a release, perform the following steps.

   1. On `GitHub <https://github.com/>`_ set the secure environment
      variables ``PYPI_USERNAME`` and ``PYPI_PASSWORD`` to ``__token__`` and a respective PyPI API token.
   2. Tag your latest commit with the desired version and let GitHub handle
      the release.

        ```shell
        git tag 0.1.0
        git push origin 0.1.0
        ```

## Copyright
{% if cookiecutter.license == "MIT" %}
* Copyright © {{ cookiecutter.year }} {{ cookiecutter.full_name }}.
* Free software distributed under the [MIT License](../LICENSE).
{% elif cookiecutter.license == "BSD-3-Clause" %}
* Copyright © {{ cookiecutter.year }} {{ cookiecutter.full_name }}.
* Free software distributed under the [3-Clause BSD License](../LICENSE).
{% elif cookiecutter.license == "Apache-2.0" %}
* Copyright © {{ cookiecutter.year }} {{ cookiecutter.full_name }}.
* Free software distributed under the [Apache Software License 2.0](../LICENSE).
{% else %}
* Copyright © {{ cookiecutter.year }} {{ cookiecutter.full_name }}. All rights reserved.
{% endif %}
