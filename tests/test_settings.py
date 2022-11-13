import io

from rich.console import Console

from pman.output import Output
from pman.settings import dump_config


def test_prompt_fuzzy_choice(assert_against_cache):
    console = Console(file=io.StringIO())
    dump_config(output=Output(console))

    result = console.file.getvalue()

    assert 'PMAN_DOC_PATH' in result
