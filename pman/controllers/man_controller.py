"""Man Controller."""

from cement import Controller, ex

from ..core.exceptions import NoManpageMatch
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
        help='Open personal manpage for provided subcommand', arguments=[
            (
                ['man_name'],
                {'help': 'Manpage Name (i.e. "rg" for "rg.md")'},
            ),
        ],
    )
    def man(self) -> None:  # FIXME: Rename to 'show'
        """Find manpage by name."""
        man_name = self.app.pargs.man_name
        try:
            man_action(man_name=man_name)
        except NoManpageMatch as exc:
            print(exc)  # FIXME: Use rich?
