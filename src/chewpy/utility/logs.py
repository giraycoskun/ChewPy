"""
Configuration utilities for logging using loguru.

Provides functions to set up console and file logging with customizable formats and log levels.
"""

import sys

from loguru import logger

CONSOLE_LOGGER_ID = None


def configure_logging(debug: bool = False, log_file: str | None = None):
    """Configure logging for the application.

    Args:
        debug (bool, optional): Enable debug logging. Defaults to False.
        log_file (str | None, optional): Path to the log file. Defaults to None.
    """
    # Remove default handler
    logger.remove()

    # Console logging
    global CONSOLE_LOGGER_ID  # # pylint: disable=global-statement
    CONSOLE_LOGGER_ID = logger.add(
        sink=sys.stdout,
        level="DEBUG" if debug else "INFO",
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>",
    )

    # File logging (rotating)
    if log_file:
        logger.add(
            log_file,
            rotation="10 MB",
            retention="7 days",
            compression="zip",
            level="DEBUG",
            enqueue=True,  # Safe for multi-process
            backtrace=True,
            diagnose=True,
        )

    return


def set_logger_verbose():
    """Set the logger to verbose mode (DEBUG level)."""
    global CONSOLE_LOGGER_ID  # pylint: disable=global-statement
    logger.remove(CONSOLE_LOGGER_ID)
    CONSOLE_LOGGER_ID = logger.add(
        sink=sys.stdout,
        level="DEBUG",
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>",
    )
