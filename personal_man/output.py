"""User-facing Output."""

from pathlib import Path

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
    def __rich_console__(self, console: Console, _options: ConsoleOptions) -> RenderResult:
        """Don't left align or box-border any of the headers."""
        yield Text('#' * self.level + ' ') + self.text


class CustomMarkdown(Markdown):

    def __init__(self, *args, **kwargs):  # type: ignore[no-untyped-def]
        self.elements['heading'] = CustomHeading
        super().__init__(*args, **kwargs)


# ======================================================================================
# Wrap rich and questionary for single Output interface

_CELL_TYPE = str  # pylint: disable=invalid-name


class Output:

    # console: Console = Field(default_factory=lambda: Console())

    def __init__(self, console: Console | None = None) -> None:
        # FIXME: Convert to BaseModel and add a validator for Console
        self.console = console or Console()

    @beartype
    def write(self, msg: str, style: str = '') -> None:
        """Supports rich-cli formatting, but whole line styling is preferred."""
        self.console.print(msg, style=style)

    @beartype
    def write_new_line(self) -> None:
        """Print a new line."""
        self.write('')

    @beartype
    def write_md(self, path_md: Path) -> None:
        """Write markdown to the output destination."""
        # TODO: provide option for PAGER, where path (instead of content) is passed?
        #   rich's built-in pager, doesn't pass the "--language md" necessary for bat
        # # with console.pager(style=True):
        # #     console.print(man_path.read_text())
        # from calcipy.proc_helpers import run_cmd
        # out = run_cmd(f'$PAGER {man_path.as_posix()}')
        # # ^ But, can't use run_cmd because it pipes STDOUT...

        with path_md.open() as man_file:
            markdown = CustomMarkdown(man_file.read())  # type: ignore[no-untyped-call]
        self.console.print(markdown)

    @beartype
    def write_table(self, columns: list[_CELL_TYPE], rows: list[list[_CELL_TYPE]]) -> None:
        """Display a markdown table based on provided cells."""
        table = Table(show_header=True, header_style='bold')
        for col in columns:
            table.add_column(col)
        for row in rows:
            table.add_row(*row)
        self.console.print(table)

    # @beartype
    # def write_df(self, df_table: pd.DataFrame, row_labels: list[str]) -> None:
    #     """Display a markdown table based on provided dataframe."""
    #     df_table = df_table.replace({np.nan: '—'})
    #     table = Table(show_header=True)
    #
    #     if row_labels:
    #         table.add_column(row_labels[0])
    #     for column in df_table.columns:
    #         table.add_column(str(column))
    #
    #     if row_labels:
    #         for label, record in zip(row_labels[1:], df_table.to_dict(orient='records')):
    #             values = [str(val) for val in (label, *record.values())]
    #             table.add_row(*values)
    #     else:
    #         for record in df_table.to_dict(orient='records'):
    #             table.add_row(*map(str, record.values()))
    #
    #     self.console.print(table)
    #
    # @beartype
    # def write_df_t(self, df_table: pd.DataFrame) -> None:
    #     """Typically used with 'df.sample(..)' to show a subset of the full table."""
    #     self.table(df_table.T, row_labels=[' ', *df_table.columns])

    @beartype
    def ask(self, question: str, choices: list[str]) -> str:
        """Ask user for selection from choices."""
        if selection := questionary.select(question, choices=choices).ask():
            return str(selection)
        raise RuntimeError(f'No option selected for: "{question}"')

    @beartype
    def ask_rich(self, question: str, choices: list[str]) -> str:
        """Alternative to questionary to prompt with rich."""
        for idx, choice in enumerate(choices):
            self.console.print(f'{idx}. {choice}')
        selection = Prompt.ask(
            question,
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
