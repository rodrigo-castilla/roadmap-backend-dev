# Dependencies

## Basics

On python we use 3 principal things:

- venv -> virtual environment for running python project
- pip -> some package manager
- pyproject.toml -> some list of dependencies, packages, version...

## Structure

Here, we are using de `src/layout` [structure](../../README.md) for this project.

## Venv

First, is to setup the `venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip --version # Optional
```

## Pyproject

Then, we can write our [`pyproject.toml`](../pyproject.toml) where its recommended to use a **build-backend** (e.g: setuptools.build_meta).
At the TOML file we have the following structure:

- build-system (Required) -> defines the backend builder
- project (Recommended) -> defines the metadata of project
  - dependencies = [...]

### Setup

Then, we can setup our project:

```bash
# inside of venv && directory of pyproject.toml
pip install -e . # install the project in "hot-install"
```

### CRUD

If we want to uninstall some dependency:

```bash
pip uninstall <dependency> # necessary with "pip"
# remove dependency from pyproject.toml
pip install -e .
```

We can take a "snapshot" of downloaded dependencies:

```bash
pip freeze > requirements.txt
```

Also, we can list all dependencies:

```bash
pip list
```

## Resources

- [venv](https://docs.python.org/3/library/venv.html)
- [manage packages](https://packaging.python.org/en/latest/tutorials/managing-dependencies/)
- [build backend](https://pydevtools.com/handbook/explanation/what-is-a-build-backend/)
- [pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
