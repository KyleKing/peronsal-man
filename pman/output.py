"""User-facing Output."""

from pathlib import Path

import numpy as np
import pandas as pd
import questionary
from beartype import beartype
from rich.console import Console, ConsoleOptions, RenderResult
from rich.markdown import Heading, Markdown
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

# ======================================================================================
# Customize rich


class CustomHeading(Heading):
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        """# Don't left align or box-border any of the headers."""
        yield Text('#' * self.level + ' ') + self.text


class CustomMarkdown(Markdown):

    def __init__(self, *args, **kwargs):
        self.elements['heading'] = CustomHeading
        super().__init__(*args, **kwargs)


# ======================================================================================
# Wrap rich and questionary for single Output interface


class Output:

    # console: Console = Field(default_factory=lambda: Console())

    def __init__(self) -> None:
        # FIXME: Convert to BaseModel and add a validator for Console
        self.console = Console()

    @beartype
    def write(self, msg: str, styles: str = '') -> None:
        """Supports rich-cli formatting, but whole line styling is preferred."""
        self.console.print(msg, styles)

    @beartype
    def write_new_line(self) -> None:
        """Print a new line."""
        self.write('\n')

    @beartype
    def write_md(self, path_md: Path) -> None:
        """Write markdown to the output destination."""
        # TODO: provide option for PAGER, where path (instead of content) is passed?
        #   rich's built-in pager, doesn't pass the "--language md" necessary for bat
        # # > with console.pager(styles=True):
        # # >     console.print(man_path.read_text())
        # > from calcipy.proc_helpers import run_cmd
        # > out = run_cmd(f'$PAGER {man_path.as_posix()}')
        # # ^ But, can't use run_cmd because it pipes STDOUT...

        with path_md.open() as man_file:
            markdown = CustomMarkdown(man_file.read())
        self.console.print(markdown)

    @beartype
    def table(self, df_table: pd.DataFrame, row_labels: list[str]) -> None:
        """Display a markdown table based on provided dataframe."""
        df_table = df_table.replace({np.nan: '—'})
        table = Table(show_header=True)

        if row_labels:
            table.add_column(row_labels[0])
        for column in df_table.columns:
            table.add_column(str(column))

        if row_labels:
            for label, record in zip(row_labels[1:], df_table.to_dict(orient='records')):
                values = [str(val) for val in (label, *record.values())]
                table.add_row(*values)
        else:
            for record in df_table.to_dict(orient='records'):
                table.add_row(*map(str, record.values()))

        self.console.print(table)

    @beartype
    def t_table(self, df_table: pd.DataFrame) -> None:
        """Typically used with 'df.sample(..)' to show a subset of the full table."""
        self.table(df_table.T, row_labels=[' ', *df_table.columns])

    @beartype
    def ask(self, question: str, choices: list[str]) -> str:
        """Ask user for selection from choices."""
        if selection := questionary.select(question, choices=choices).ask():
            return selection
        raise RuntimeError(f'No option selected for: "{question}"')

    @beartype
    def ask_rich(self, question: str, choices: list[str]) -> str:
        """Alternative to questionary to prompt with rich."""
        for idx, choice in enumerate(choices):
            self.console.print(f'{idx}. {choice}')
        selection = Prompt.ask(
            'Which manpage would you like to see?',
            choices=[*map(str, range(len(choices)))],
            default='0',
        )
        return choices[int(selection)]

    @beartype
    def ask_file(self, question: str, base_dir: Path, files: list[Path]) -> Path:
        """Convenience wrapper around ask to show only the relative path when asking."""
        choices = [pth.relative_to(base_dir).as_posix() for pth in files]
        selection = self.ask(question, sorted(choices))
        return base_dir / selection
