"""personal_man."""

from loguru import logger

__version__ = '1.1.1'
__pkg_name__ = 'personal_man'

logger.disable(__pkg_name__)

# ====== Above is the recommended code from calcipy_template and may be updated on new releases ======

# Load entry point for CLI
from .cli import run  # noqa: E402

__all__ = ('run',)
