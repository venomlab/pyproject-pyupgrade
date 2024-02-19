import logging
import subprocess
import sys

from pyproject_pyupgrade.config import find_config_from_cwd


def cli() -> None:
    logger = logging.getLogger("pyproject-pyupgrade")
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)
    config = find_config_from_cwd()
    args = list(config.flags)
    cli_args = sys.argv[1:]
    for arg in cli_args:
        if arg not in args:
            args.append(arg)
    if "--pyproject-pyupgrade-debug" in args:
        logger.setLevel(logging.DEBUG)
        args.remove("--pyproject-pyupgrade-debug")
    subprocess_args = ["pyupgrade", *args]
    logger.debug("parsed config: %s", config)
    logger.debug("cli args: %s", cli_args)
    logger.debug("calling pyupgrade with following arguments: %s", subprocess_args)
    result = subprocess.run(subprocess_args)
    sys.exit(result.returncode)
