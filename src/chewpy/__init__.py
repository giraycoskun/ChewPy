"""ChewPy
This module serves as the main entry point for the ChewPy CLI application.

It initializes secret configuration, sets up logging based on environment variables,
and launches the command-line interface using Typer. Logging is handled via Loguru,
and secrets are managed through utility functions.

Typical usage:
    python -m chewpy
    uv run python -m chewpy

Functions:
    main(): Initializes configuration and runs the CLI app.
"""

from loguru import logger

from chewpy.commands import app
from chewpy.utility.secrets import configure_secrets, get_secret
from chewpy.utility.logs import configure_logging

ENV_DEBUG = True


def main() -> None:
    """Main entry point for the CLI."""
    global ENV_DEBUG  # pylint: disable=global-statement
    configure_secrets()
    try:
        ENV_DEBUG = get_secret("DEBUG", default=False, is_bool=True)
    except KeyError as e:
        logger.warning(e)
        ENV_DEBUG = False
    configure_logging(debug=ENV_DEBUG)

    logger.info("main from ChewPy!")
    app()


if __name__ == "__main__":
    main()
