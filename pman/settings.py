"""pman Settings"""

from typing import Optional

from beartype import beartype
from pydantic import BaseSettings, DirectoryPath
from rich.console import Console
from rich.table import Table


class Settings(BaseSettings):
    """Configurable Settings (Environment Variables)."""

    DOC_PATH: Optional[DirectoryPath]

    SEARCH_TOOL: str = 'grep'

    class Config:
        case_sensitive = True
        env_prefix = 'PMAN_'


@beartype
def dump_config() -> None:
    """Dump pman configuration."""
    key_lookup = (
        ('PMAN_DOC_PATH', Settings().DOC_PATH or ''),
        ('PMAN_SEARCH_TOOL', Settings().SEARCH_TOOL),
    )

    console = Console()
    table = Table(show_header=True, header_style='bold')
    table.add_column('Environment Variable')
    table.add_column('Value')
    for key_name, value in key_lookup:
        table.add_row(key_name, value)
    console.print(table)
