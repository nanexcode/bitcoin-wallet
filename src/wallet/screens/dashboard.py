from textual.app import ComposeResult
from textual.widgets import Static, TabPane, Label, TabbedContent
from .overview import Overview
from .receive import Receive
from .send import Send
from .transactions import Transactions

class Dashboard(Static):
    """
        Shows a grid with the prices of all the cryptocurrencies
    """

    DEFAULT_CSS = """
    Dashboard {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent(initial="overview"):
            with TabPane("Overview", id="overview"):
                yield Overview()
            with TabPane("Send", id="send"):
                yield Send()
            with TabPane("Receive", id="receive"):
                yield Receive()
            with TabPane("Transactions", id="transactions"):
                yield Transactions()

    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab
