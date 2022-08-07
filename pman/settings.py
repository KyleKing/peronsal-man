"""
https://pydantic-docs.helpmanual.io/usage/settings/

"""

from enum import Enum
from typing import Optional

from beartype import beartype
from pydantic import BaseSettings, Field, DirectoryPath
from rich.console import Console
from rich.table import Table


class Pagers(Enum):

    os_pager = ''
    python = 'python'


class Settings(BaseSettings):

    DOC_PATH: Optional[DirectoryPath]

    FIND_TOOL: str = 'find'
    SEARCH_TOOL: str = 'grep'

    PAGER: Pagers = Pagers.python
    SYSTEM_PAGER: str = Field(env='PAGER')

    class Config:
        case_sensitive = True
        env_prefix = 'PMAN_'


@beartype
def dump_config() -> None:
    """Dump pman configuration."""
    key_lookup = (
        ('PMAN_DOC_PATH', Settings().DOC_PATH or ''),
        ('PMAN_FIND_TOOL', Settings().FIND_TOOL),
        ('PMAN_SEARCH_TOOL', Settings().SEARCH_TOOL),
        ('PMAN_PAGER', Settings().PAGER.value),
        ('PAGER (Fallback)', Settings().SYSTEM_PAGER or ''),
    )

    console = Console()
    table = Table(show_header=True, header_style='bold')
    table.add_column('Environment Variable')
    table.add_column('Value')
    for key_name, value in key_lookup:
        table.add_row(key_name, value)
    console.print(table)


dump_config()
