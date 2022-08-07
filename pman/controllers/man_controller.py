"""Man Controller."""

from cement import Controller, ex

from ..man import man_action


class ManController(Controller):
    """man CLI Controller."""

    class Meta:
        label = 'man'

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
    def man(self) -> None:
        """Find manpage by name."""
        pargs = self.app.pargs
        man_action(search_token=pargs.search_token)
