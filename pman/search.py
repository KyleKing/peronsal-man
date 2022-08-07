"""Search."""

import subprocess

from beartype import beartype

from .settings import SETTINGS


@beartype
def search_action(*, search_token: str) -> None:
    subprocess.run(
        f'rg --type=md "{search_token}" "{SETTINGS.DOC_PATH.as_posix()}"',
        shell=True,
    )
