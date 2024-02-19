# Pyproject pyupgrade

pyproject.toml configuration wrapper for [pyupgrade](https://github.com/asottile/pyupgrade)

## Installation

Via pip

```shell
pip install pyproject-pyupgrade
```

Via poetry

```shell
poetry add --group dev pyproject-pyupgrade
```

Via pipx

```shell
pipx install -f pyproject-pyupgrade
```

## Usage

Make sure you have a desired version of [pyupgrade](https://github.com/asottile/pyupgrade)
installed in your python environment.

Add the following section in your `pyproject.toml`:

```toml
[tool.pyupgrade]
# for example, if you're using python 3.10
py310-plus = true
```

And then just execute it via CLI

```shell
pyproject-pyupgrade [filename [filenames...]]
```

or shorter version

```shell
ppyupgrade [filename [filenames...]]
```

So, basically you specify flags that you want to add to `pyupgrade`
CLI arguments specifying them without leading two dashes (`--`).
This is the way how you can supply any option that `pyupgrade` receives
no matter which version of it you're using

There is also one additional parameter provided exclusively by `pyproject-pyupgrade` wrapper:

```toml
[tool.pyupgrade]
pyproject-pyupgrade-debug = true
```

Or directly via CLI

```shell
ppyupgrade --pyproject-pyupgrade-debug ...
```

This option is going to output debug information about `pyproject-pyupgrade`.
Info about parsed configuration from pyproject.toml (if there is one) and all the flags

## As a pre-commit hook

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions.

Sample `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/venomlab/pyproject-pyupgrade
    rev: v0.1.0
    hooks:
      - id: ppyupgrade
```
