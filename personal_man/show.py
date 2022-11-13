"""show."""

import subprocess  # noqa: S404  # nosec
from pathlib import Path

from beartype import beartype

from .core.exceptions import NoManpageMatch
from .output import Output
from .settings import SETTINGS


@beartype
def get_files(doc_dir: Path, man_name: str | None = None) -> list[Path]:
    """Return all files matching the optional search string in `doc_dir`."""
    pattern = f'*{man_name}*' if man_name else '*'
    return [*sorted(doc_dir.rglob(f'{pattern}.md'))]


@beartype
def match_man(*, man_name: str) -> Path:
    """Match the request personal manpage."""
    doc_dir = SETTINGS.DOC_PATH
    matches = get_files(doc_dir, man_name)
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
def ls_man() -> None:
    """List the possible man files."""
    matches = get_files(SETTINGS.DOC_PATH)
    output = Output()
    output.write('\n'.join(map(str, matches)))
    output.write_new_line()


@beartype
def show_man(*, man_path: Path) -> None:
    """Dump the manpage for the user."""
    output = Output()
    output.write_md(man_path)
    output.write_new_line()


@beartype
def edit_man(*, man_path: Path) -> None:
    """Open the manpage for the user in their `$EDITOR`."""
    subprocess.run(  # nosec  # nosemgrep
        f'$EDITOR "{man_path}"', shell=True, check=True,  # noqa: S602
    )


@beartype
def show_action(*, man_name: str | None, edit: bool) -> None:
    """Full action for recognizing the user-requested personal-manpage."""
    if man_name:
        man_path = match_man(man_name=man_name)
        if edit:
            edit_man(man_path=man_path)
        else:
            show_man(man_path=man_path)
    else:
        ls_man()
