from textual.app import ComposeResult
from textual.widgets import Static, Label
from textual.containers import Container, Center
from rich.table import Table
from rich.style import Style
from services import WalletService


class TransactionDetails:

    def __init__(self):
        self.wallet = WalletService("my_wallet", "testnet")

    def create_panel(self) -> Table:
        transactions_table = Table(title="Recent Transactions",
                                   title_style=Style(color="#bbc8e8", bold=True))

        transactions_table.add_column("Status")
        transactions_table.add_column("Hash")
        transactions_table.add_column("Amount", style="green", justify="right")
        transactions_table.add_column("Conf")

        txs = self.wallet.get_transactions()

        for tx in txs:
            status = "❌"
            if tx.confirmations >= 1:
                status = "✅"

            transactions_table.add_row(status,
                                       tx.tx_id,
                                       tx.value,
                                       str(tx.confirmations))
        return transactions_table


class RecentTransactions(Static):
    DEFAULT_CSS = """
        RecentTransactions {
            width: 100%
        }
        
        #transactions-table-main-container {
            width: 100%;
        }
        
        #transactions-table-center-container {
            width: 100%;
        }

    """

    def __init__(self):
        super().__init__()
        self.data_table_provider = TransactionDetails()

    def compose(self) -> ComposeResult:
        yield Container(
            Center(
                Static(id="transactions-table"),
                id="transactions-table-center-container"
            ),
            id="transactions-table-main-container"
        )

    def on_mount(self) -> None:
        self.update_table()


    def update_table(self):
        transactions = self.query_one("#transactions-table")
        transactions.update(self.data_table_provider.create_panel())