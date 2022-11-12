"""pman Settings."""

from os import environ
from pathlib import Path
from typing import Optional

from beartype import beartype
from pydantic import BaseSettings, DirectoryPath, Field
from rich.console import Console
from rich.table import Table

# FIXME: Implement a wrapper of rich that abstracts common operations
#   so that no code is dependent on the rich library
#   Examples: cli_print, cli_table, cli_prompt, etc.

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
def dump_config(console: Optional[Console]) -> None:
    """Dump pman configuration."""
    if not console:
        console = Console()
    pman_doc_path = SETTINGS.DOC_PATH.as_posix() if SETTINGS.DOC_PATH else ''
    key_lookup = (
        ('PMAN_DOC_PATH', pman_doc_path),
        ('PMAN_SEARCH_TOOL', SETTINGS.SEARCH_TOOL),
    )

    table = Table(show_header=True, header_style='bold')
    table.add_column('Environment Variable')
    table.add_column('Value')
    for key_name, value in key_lookup:
        table.add_row(key_name, value)
    console.print(table)
