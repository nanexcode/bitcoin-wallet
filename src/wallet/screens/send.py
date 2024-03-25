from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Vertical
from .widgets import LabelledInput


class Send(Static):
    """
        Shows a grid with the prices of all the cryptocurrencies
    """

    DEFAULT_CSS = """
    Send {
        align: center middle;
    }
    
    #send-vertical-layout {
        align: center middle;
    }
    
    """

    def compose(self) -> ComposeResult:
        yield Vertical(
            LabelledInput("Send To"),
            LabelledInput("Label"),
            LabelledInput("Quantity"),
            id="send-vertical-layout"
        )

