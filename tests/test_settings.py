import io

from rich.console import Console

from personal_man.output import Output
from personal_man.settings import dump_config


def test_prompt_fuzzy_choice():
    console = Console(file=io.StringIO())
    dump_config(output=Output(console))

    result = console.file.getvalue()

    assert 'PMAN_DOC_PATH' in result
