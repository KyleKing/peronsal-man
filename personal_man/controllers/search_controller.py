"""Search Controller."""

import subprocess  # noqa: S404  # nosec

from cement import Controller, ex

from ..output import Output
from ..search import search_action

HELP_TEXT = 'Search personal manpage body text'


class SearchController(Controller):  # type: ignore[misc]  # pylint: disable=R0901
    """Search CLI Controller."""

    class Meta:
        label = 'search'

    def _default(self) -> None:
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(  # type: ignore[misc]
        help=HELP_TEXT, arguments=[
            (
                ['search_token'],
                {'help': 'Search string'},
            ),
        ],
    )
    def search(self) -> None:
        """Find manpage by searching with a regular expression or text string."""
        search_token = self.app.pargs.search_token
        try:
            search_action(search_token=search_token)
        except subprocess.CalledProcessError as exc:
            output = Output()
            output.write(repr(exc))
            output.write(f'No matches found for search of: {search_token}', style='red')
            output.write_new_line()
            self.app.exit_code = 1
