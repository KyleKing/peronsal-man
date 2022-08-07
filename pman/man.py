"""man."""

from pathlib import Path

from beartype import beartype
from rich.console import Console, ConsoleOptions, RenderResult
from rich.markdown import Heading, Markdown
from rich.prompt import Prompt
from rich.text import Text

from .core.exceptions import NoManpageMatch
from .settings import SETTINGS


class CustomHeading(Heading):
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        """# Don't left align or box-border any of the headers."""
        yield Text('#' * self.level + ' ') + self.text


class CustomMarkdown(Markdown):

    def __init__(self, *args, **kwargs):
        self.elements['heading'] = CustomHeading
        super().__init__(*args, **kwargs)


@beartype
def match_man(*, search_token: str) -> Path:
    """Match the request personal manpage."""
    doc_dir = SETTINGS.DOC_PATH
    matches = [*doc_dir.glob(f'*{search_token}*.md')]

    if len(matches) > 1:
        choices = [match.relative_to(doc_dir).as_posix() for match in matches]
        selection = Prompt.ask(
            'Which manpage would you like to see?',
            choices=choices,
            default=choices[0],
        )
        return doc_dir / selection
    elif len(matches) == 1:
        return matches[0]

    raise NoManpageMatch(f'No known personal-manpage for {search_token}.md')


@beartype
def dump_man(*, man_path: Path) -> None:
    """Dump the manpage for the user."""
    console = Console()

    # TODO: provide option for PAGER, where path (instead of content) is passed?
    #   rich's built-in pager, doesn't pass the "--language md" necessary for bat
    # with console.pager(styles=True):
    #     console.print(man_path.read_text())

    with open(man_path) as man_file:
        markdown = CustomMarkdown(man_file.read())
    console.print(markdown)
    console.print('\n')


@beartype
def man_action(*, search_token: str) -> None:
    """Full action for recognizing the user-requested personal-manpage."""
    # TODO: User try/except block to prompt user if they want to create the manpage when not found
    #   https://github.com/KyleKing/personal-man/issues/4

    man_path = match_man(search_token=search_token)
    dump_man(man_path=man_path)
