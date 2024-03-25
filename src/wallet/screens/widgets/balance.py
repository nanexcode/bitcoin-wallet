from textual.app import ComposeResult
from textual.widgets import Static, Label
from textual.containers import Grid


class Balance(Static):
    DEFAULT_CSS = """
    Balance {
        align: center middle;
    }

    #balance-grid-container {
        grid-size: 2 3;
        padding: 0 1;
        border: green;
        background: black;
    }
    """

    def compose(self) -> ComposeResult:
        yield Grid(
                Label("Available"),
                Label("1.23456768 BTC"),
                Label("Pending"),
                Label("0.0000000 BTC"),
                Label("Total"),
                Label("1.23456768 BTC"),
                id="balance-grid-container"
            )
