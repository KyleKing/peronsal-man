"""pman."""

from loguru import logger

__version__ = '1.0.0'
__pkg_name__ = 'pman'

logger.disable(__pkg_name__)

# ====== Above is the recommended code from calcipy_template and may be updated on new releases ======

# Load entry point for CLI
from .cli import run  # noqa: E402

__all__ = ('run',)
