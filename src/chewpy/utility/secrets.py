"""Utility functions for managing secrets."""

import os
from typing import Any

from loguru import logger
import dotenv


def configure_secrets() -> None:
    """Configures the secrets management by loading environment variables."""
    # TODO: Create env file if not exists
    dotenv.load_dotenv()
    # try:
    #     env_file_path = dotenv.find_dotenv(raise_error_if_not_found=True)
    # except IOError:
    #     logger.warning("Could not find .env file. Creating at ..")


def set_env_variable(key: str, value: str) -> None:
    """
    Sets an environment variable to the specified value.

    Args:
        key (str): The name of the environment variable to set.
        value (str): The value to assign to the environment variable.
    """
    os.environ[key] = value


def get_secret(
    key: str, default: Any = None, is_bool: bool = False, is_int: bool = False
) -> Any:  # type: ignore
    """
    Retrieves a secret from environment variables.

    Args:
        key (str): The name of the environment variable.
        default (str, optional): Fallback value if key is not found.
        is_bool (bool, optional): Whether to cast the value to a boolean.
        is_int (bool, optional): Whether to cast the value to an integer.
    Returns:
        Any: The value of the environment variable or default if not found.
    """
    value = os.getenv(key, default)
    if is_bool:
        value = value.lower() in ("true", "1")
    elif is_int:
        try:
            value = int(value)
        except ValueError as exc:
            logger.error(f"Missing/incorrect key {key}")
            raise KeyError(f"Missing/incorrect key: {key}") from exc
    return value


def write_secret(key: str, value: str) -> None:
    """
    Writes a secret to the environment variables.

    Args:
        key (str): The name of the environment variable.
        value (str): The value to assign to the environment variable.
    """
    os.environ[key] = value
