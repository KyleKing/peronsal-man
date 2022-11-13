"""show."""

from pathlib import Path

from beartype import beartype

from .core.exceptions import NoManpageMatch
from .output import Output
from .settings import SETTINGS


@beartype
def match_man(*, man_name: str) -> Path:
    """Match the request personal manpage."""
    doc_dir = SETTINGS.DOC_PATH
    matches = [*doc_dir.glob(f'*{man_name}*.md')]

    if len(matches) > 1:
        output = Output()
        return output.ask_file('Which manpage would you like to see?', doc_dir, matches)
    if len(matches) == 1:
        return matches[0]
    raise NoManpageMatch(
        f'No known personal-manpage for {man_name}.md. Try creating a new one with:'
        f' `tldr {man_name} > $PMAN_DOC_PATH/{man_name}.md` or use `man` or `--help`',
    )


@beartype
def show_man(*, man_path: Path) -> None:
    """Dump the manpage for the user."""
    output = Output()
    output.write_md(man_path)
    output.write_new_line()


@beartype
def show_action(*, man_name: str | None) -> None:
    """Full action for recognizing the user-requested personal-manpage."""
    if not man_name:
        raise NotImplementedError('Print a list of all known manpages!')

    man_path = match_man(man_name=man_name)
    show_man(man_path=man_path)
