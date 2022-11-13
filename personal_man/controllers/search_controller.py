"""Search Controller."""

from cement import Controller, ex

from ..search import search_action

HELP_TEXT = 'Search personal manpage body text'


class SearchController(Controller):  # pylint: disable=R0901
    """Search CLI Controller."""

    class Meta:
        label = 'search'

        arguments = []
        """Controller level arguments. ex: 'pman --version'."""

    def _default(self) -> None:
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(
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
        search_action(search_token=search_token)
