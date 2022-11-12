"""man."""

# FIXME: What is a better name for file search?

from pathlib import Path
from typing import Optional

from beartype import beartype
from rich.console import Console, ConsoleOptions, RenderResult
from rich.markdown import Heading, Markdown
from rich.prompt import Prompt
from rich.text import Text

from .core.exceptions import NoManpageMatch
from .settings import SETTINGS

# ======================================================================================
# Customize rich


class CustomHeading(Heading):
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        """# Don't left align or box-border any of the headers."""
        yield Text('#' * self.level + ' ') + self.text


class CustomMarkdown(Markdown):

    def __init__(self, *args, **kwargs):
        self.elements['heading'] = CustomHeading
        super().__init__(*args, **kwargs)


# ======================================================================================
# manpage interaction


@beartype
def match_man(*, man_name: str) -> Path:
    """Match the request personal manpage."""
    doc_dir = SETTINGS.DOC_PATH
    matches = [*doc_dir.glob(f'*{man_name}*.md')]

    choices = ['fix', 'feat', 'docs']

    if len(matches) > 1:
        choices = [match.relative_to(doc_dir).as_posix() for match in matches]
        # TODO: Sort alphabetically && rank choices based on closeness to exact match?

        # FIXME: Consider https://github.com/tmbo/questionary
        console = Console()
        for idx, choice in enumerate(choices):
            console.print(f'{idx}. {choice}')
        selection = Prompt.ask(
            'Which manpage would you like to see?',
            choices=[*map(str, range(len(choices)))],
            default='0',
        )
        return doc_dir / choices[int(selection)]

    if len(matches) == 1:
        return matches[0]

    raise NoManpageMatch(f'No known personal-manpage for {man_name}.md')


@beartype
def dump_man(*, man_path: Path) -> None:
    """Dump the manpage for the user."""
    console = Console()

    # TODO: provide option for PAGER, where path (instead of content) is passed?
    #   rich's built-in pager, doesn't pass the "--language md" necessary for bat
    # # # with console.pager(styles=True):
    # # #     console.print(man_path.read_text())
    # from calcipy.proc_helpers import run_cmd
    # out = run_cmd(f'$PAGER {man_path.as_posix()}')
    # # ^ But, can't use run_cmd because it pipes STDOUT...

    with man_path.open() as man_file:
        markdown = CustomMarkdown(man_file.read())
    console.print(markdown)
    console.print('\n')


@beartype
def man_action(*, man_name: Optional[str]) -> None:
    """Full action for recognizing the user-requested personal-manpage."""
    if not man_name:
        raise NotImplementedError('Print a list of all known manpages!')

    # TODO: User try/except block to prompt user if they want to create the manpage when not found
    #   https://github.com/KyleKing/personal-man/issues/4

    man_path = match_man(man_name=man_name)
    dump_man(man_path=man_path)
