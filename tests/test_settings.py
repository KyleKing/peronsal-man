import io

from rich.console import Console

from pman.settings import dump_config


def test_prompt_fuzzy_choice():
    console = Console(file=io.StringIO())
    expected = '...'
    dump_config(console=console)

    result = console.file.getvalue()

    print(repr(result))
    assert result == expected
