"""`show` CLI Controller."""

from cement import Controller, ex

from ..core.exceptions import NoManpageMatch
from ..show import show_action

HELP_TEXT = 'Show the personal manpage matching the provided argument or select from nearest matches'  # noqa: Q440


class ShowController(Controller):  # pylint: disable=R0901
    """`show` CLI Controller."""

    class Meta:
        label = 'show'

        arguments = []
        """Controller level arguments. ex: 'pman --version'."""

    def _default(self) -> None:
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(
        help=HELP_TEXT, arguments=[
            (
                ['man_name'],
                {'help': 'Personal Manpage Name (i.e. "rg" for "rg.md")'},
            ),
        ],
    )
    def show(self) -> None:
        """Find manpage by name."""
        man_name = self.app.pargs.man_name
        try:
            show_action(man_name=man_name)
        except NoManpageMatch as exc:
            print(exc)  # FIXME: Use rich?
