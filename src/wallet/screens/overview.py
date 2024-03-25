from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Grid
from .widgets import Balance, RecentTransactions


class Overview(Static):
    DEFAULT_CSS = """
    Overview {
        align: center middle;
    }

    #overview-screen-container {
        grid-size: 2 1;
        padding: 0 1;
        border: thick $background 80%;
        background: $surface;
    }
    """

    def compose(self) -> ComposeResult:
        yield Grid(
            Balance(),
            RecentTransactions(),
            id="overview-screen-container"
        )

    def on_mount(self):
        pass

    def load_widgets(self):
        pass
