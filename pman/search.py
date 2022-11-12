"""Search."""

import subprocess  # noqa; S404

from beartype import beartype

from .settings import SETTINGS


@beartype
def search_action(*, search_token: str) -> None:
    subprocess.run(
        f'rg --type=md "{search_token}"', cwd=SETTINGS.DOC_PATH,
        shell=True, check=True,  # noqa: S602
    )
