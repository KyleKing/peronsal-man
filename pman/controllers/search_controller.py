"""Search Controller."""

from cement import Controller, ex

from ..search import search_action


class SearchController(Controller):
    """Search CLI Controller."""

    class Meta:
        label = 'search'

        arguments = []
        """Controller level arguments. ex: 'pman --version'."""

    def _default(self) -> None:
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(
        help='Find Subcommand', arguments=[
            (
                ['-t', '--search-token'],
                {'help': 'Search token', 'action': 'store', 'dest': 'search_token'},
            ),
        ],
    )
    def search(self) -> None:
        """Find manpage by searching with a regular expression or text string."""
        pargs = self.app.pargs
        search_action(search_token=pargs.search_token)
