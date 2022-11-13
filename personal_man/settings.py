"""personal_man Settings."""

from os import environ
from pathlib import Path

from beartype import beartype
from pydantic import BaseSettings, DirectoryPath, Field

from .output import Output

DEF_DOC_PATH = Path(environ.get('XDG_DATA_HOME', '~/.local')).expanduser() / 'pman'


class Settings(BaseSettings):
    """Configurable Settings (Environment Variables)."""

    DOC_PATH: DirectoryPath = Field(default=DEF_DOC_PATH)

    SEARCH_TOOL: str = 'grep'

    class Config:
        case_sensitive = True
        env_prefix = 'PMAN_'


SETTINGS = Settings()
"""Global settings instance."""


# FIXME: Make this part of the default help output or separate subcommand
@beartype
def dump_config(output: Output | None = None) -> None:
    """Dump pman configuration."""
    output = output or Output()
    pman_doc_path = SETTINGS.DOC_PATH.as_posix()
    columns = ['Environment Variable', 'Value']
    rows = [
        ['PMAN_DOC_PATH', pman_doc_path],
        ['PMAN_SEARCH_TOOL', SETTINGS.SEARCH_TOOL],
    ]
    output.write_table(columns=columns, rows=rows)
