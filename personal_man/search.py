"""Search."""

import subprocess  # noqa: S404  # nosec

from beartype import beartype

from .settings import SETTINGS


@beartype
def search_action(*, search_token: str) -> None:
    subprocess.run(  # nosec  # nosemgrep
        f'rg --type=md "{search_token}"', cwd=SETTINGS.DOC_PATH,
        shell=True, check=True,  # noqa: S602
    )
