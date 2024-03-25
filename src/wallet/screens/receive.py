from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Vertical
from .widgets import LabelledInput


class Receive(Static):
    """
        Shows a grid with the prices of all the cryptocurrencies
    """

    DEFAULT_CSS = """
    Receive {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Vertical(
            LabelledInput("Send To"),
            LabelledInput("Label"),
            LabelledInput("Quantity"),
        )

