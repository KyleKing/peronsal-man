"""`show` CLI Controller."""

import argparse

from cement import Controller, ex

from ..core.exceptions import NoManpageMatch
from ..output import Output
from ..show import show_action

HELP_TEXT = 'Show the personal manpage matching the provided argument or select from nearest matches'  # noqa: Q440


class ShowController(Controller):  # type: ignore[misc]  # pylint: disable=R0901
    """`show` CLI Controller."""

    class Meta:
        label = 'show'

    def _default(self) -> None:
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(  # type: ignore[misc]
        help=HELP_TEXT, arguments=[
            (
                ['man_name'],
                {'help': 'Personal Manpage Name (i.e. "rg" for "rg.md")', 'nargs': '?'},
            ),
            (
                ['-e', '--edit'],
                {
                    'help': 'If set, open the manpage in `$EDITOR`',
                    'action': argparse.BooleanOptionalAction,
                    'default': False,
                },
            ),
        ],
    )
    def show(self) -> None:
        """Find manpage by name."""
        man_name = self.app.pargs.man_name
        edit = self.app.pargs.edit
        try:
            show_action(man_name=man_name, edit=edit)
        except NoManpageMatch as exc:
            output = Output()
            output.write(str(exc))
            self.app.exit_code = 1
