# pyproject pyupgrade

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

Make sure you have a desired version of `pyupgrade`
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
This is the way how you can supply any option that your version of `pyupgrade` receives

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
    rev: v0.1.1
    hooks:
      - id: ppyupgrade
```

## ToDo

- [ ] Add tests and `tox` config to run them for all supported python versions
- [ ] Add option to specify custom `pyupgrade` command. It allows in case if you want to chain pyupgrade wrappers (for instance, with [pyupgrade-directories](https://github.com/domdfcoding/pyupgrade-directories))
- [ ] Add better parser for TOML. Right now the parser is ultra primitive and might lead to errors if used improperly
- [ ] If `python` version >= `3.11` use tomllib for `pyproject.toml` parsing
- [ ] Support adding custom options or key-value arguments to `pyupgrade` CLI
- [ ] Support storing configuration in `pyupgrade.ini`
- [ ] Support storing configuration in `tox.ini`
- [ ] Support storing configuration in `setup.cfg`
