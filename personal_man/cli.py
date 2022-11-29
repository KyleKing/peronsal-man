"""pman Command Line."""

import traceback

from beartype import beartype
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from loguru import logger

from . import __pkg_name__
from .controllers.search_controller import SearchController
from .controllers.show_controller import ShowController
from .core.exceptions import CLIError
from .output import Output
from .settings import dump_config

# Initialize nested dictionary for storing application defaults
_CONFIG = init_defaults(__pkg_name__)


@beartype
def on_post_setup(app: App) -> None:
    if not app.argv:
        output = Output()
        dump_config(output)
        output.write('See full help with "pman --help"')


class CLIApp(App):  # type: ignore[misc]
    """My CLI Application."""

    class Meta:
        label = __pkg_name__

        config_defaults = _CONFIG
        """Configuration defaults."""

        exit_on_close = True
        """Call sys.exit() on close."""

        handlers = [ShowController, SearchController]
        """Register handlers."""

        hooks = [
            ('post_setup', on_post_setup),
        ]
        """Register hooks."""


class CLIAppTest(TestApp, CLIApp):  # type: ignore[misc]  # pylint: disable=R0901
    """A sub-class of CLIApp that is better suited for testing."""

    class Meta:
        label = __pkg_name__


def run() -> None:
    """Application Entry Point."""
    with CLIApp() as app:
        logger.enable(__pkg_name__)
        try:
            app.run()

        except AssertionError as exc:
            logger.error(f'AssertionError > {exc.args[0]}')  # noqa: TC400
            app.exit_code = 1

            if app.debug is True:
                traceback.print_exc()

        except CLIError as exc:
            logger.error(f'CLIError > {exc.args[0]}')  # noqa: TC400
            app.exit_code = 1

            if app.debug is True:
                traceback.print_exc()

        except CaughtSignal:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            logger.exception('Unhandled Exception')
            app.exit_code = 0
