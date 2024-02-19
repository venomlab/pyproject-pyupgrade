import dataclasses
import pathlib
import typing


class ConfigNotFoundError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


@dataclasses.dataclass
class Config:
    path: pathlib.Path
    flags: typing.List[str]

    @classmethod
    def empty(cls) -> "Config":
        return cls(path=pathlib.Path(), flags=[])


def find_config_from_cwd() -> Config:
    path = pathlib.Path().expanduser().absolute()
    try:
        return find_config_recursively(path)
    except ConfigNotFoundError:
        return Config.empty()


def find_config_recursively(path: pathlib.Path) -> Config:
    if not path.is_dir():
        path = path.parent
    try:
        return find_config_in_directory(path)
    except ConfigNotFoundError:
        if not path.parents:
            raise
        return find_config_recursively(path.parent)


def find_config_in_directory(path: pathlib.Path) -> Config:
    try:
        with (path / "pyproject.toml").open("r") as file:
            return parse_config_from_pyproject_toml(file)
    except OSError as ex:
        raise ConfigNotFoundError(f"{path} does not contain pyproject.toml") from ex


def parse_config_from_pyproject_toml(file: typing.TextIO) -> Config:
    flags: typing.List[str] = []
    path = pathlib.Path(file.name)
    pyupgrade_section_started = False
    for line in file:
        line = line.strip()
        if line.startswith("#"):
            continue
        if line.startswith("[tool.pyupgrade]"):
            pyupgrade_section_started = True
            continue
        if not pyupgrade_section_started:
            continue
        if line.startswith("["):
            break
        if "=" in line:
            key, value = line.split("=", maxsplit=1)
            key, value = key.strip(), value.strip()
            if value == "true":
                flags.append(f"--{key}")
            continue
    return Config(path, flags)
