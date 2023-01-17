# Cookiecutter Template for Python Packages

_Initialize a complete Python package project structure._

## Usage

### Dependencies

Create or activate a Python virtual environment. You can [read this guide to
learn more](https://realpython.com/python-virtual-environments-a-primer/) about
them and how to create one. Alternatively, particularly if you are a Windows or
Mac user, you can also use [Anaconda](https://docs.anaconda.com/anaconda/).

After creating a virtual environment, install
[cruft](https://cruft.github.io/cruft/) to create your project from this
template. Cruft also helps you to later [manage
updates](https://cruft.github.io/cruft/#updating-a-project) to the template. If
you are using a conda environment, please use `conda` instead of `pip`.

```shell
pip install cruft jinja2-strcase
```

### Create

Now you are ready to create your project by answering the template questions
that follow.

```shell
cruft create https://github.com/opencobra/cookiecutter-python-package
```

The cookiecutter project itself is provided under the [Apache Software License
2.0](https://www.apache.org/licenses/LICENSE-2.0), however, you can freely
choose the license for your generated project. MIT, BSD-3-Clause, Apache-2.0, and
proprietary code are supported out of the box, but you can replace this with
whatever license you wish, of course.

### Update

If, at a later point, you want to update your project with changes added to this
cookiecutter template, you can do so with one command from the root of your
project directory:

```shell
cruft update
```

You will get a chance to review the changes to be merged into your existing
project.

## Copyright

* Copyright © 2022, Moritz E. Beber
* Copyright © 2019-2022, openCOBRA
* Free software distributed under the [Apache Software License
  2.0](https://www.apache.org/licenses/LICENSE-2.0)
