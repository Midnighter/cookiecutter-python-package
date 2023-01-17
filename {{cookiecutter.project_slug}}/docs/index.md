# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

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
