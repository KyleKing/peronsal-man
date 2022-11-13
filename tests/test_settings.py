import io

from rich.console import Console

from pman.settings import dump_config


def test_prompt_fuzzy_choice(assert_against_cache):
    console = Console(file=io.StringIO())
    dump_config(console=console)

    result = console.file.getvalue()

    assert_against_cache(result.encode('ascii', 'ignore').decode('ascii').replace('    ', ' '))
