from textual.app import ComposeResult
from textual.widgets import Static, Label, Tab
from textual.containers import Vertical, Horizontal


class TransactionDetails(Static):

    DEFAULT_CSS = """
    LabelledInput {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Vertical(
            Horizontal(
                Label("6/13/21"),
                Label("+1.23456768 BTC")
            ),
            Horizontal(
                Label("5/8/2022"),
                Label("-0.98750000 BTC")
            ),
            Horizontal(
                Label("4/19/2023"),
                Label("+1.23456768 BTC")
            )
        )


class RecentTransactions(Static):

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label("Recent Transactions"),
            TransactionDetails(),
            TransactionDetails(),
            TransactionDetails(),
            TransactionDetails()
        )
