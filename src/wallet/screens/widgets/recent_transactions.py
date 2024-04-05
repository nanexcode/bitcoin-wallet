import time

from textual.app import ComposeResult
from textual.widgets import Static, Label
from textual.containers import Container, Center
from textual import work
from textual.worker import Worker, get_current_worker
from rich.table import Table
from rich.style import Style
from services import WalletService


class TransactionDetails:

    def __init__(self):
        self.wallet = WalletService("my_wallet", "testnet")

    def create_panel(self, width) -> Table:
        transactions_table = Table(title="Recent Transactions",
                                   title_style=Style(color="#bbc8e8", bold=True),
                                   expand=True,
                                   width=width)

        transactions_table.add_column("Status", justify="center")
        transactions_table.add_column("Hash")
        transactions_table.add_column("Amount", style="green", justify="right")
        transactions_table.add_column("Conf", justify="right")

        txs = self.wallet.get_transactions(50)

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

    async def on_mount(self) -> None:
        self.update_table()

    @work(exclusive=True, thread=True)
    def update_table(self):
        while True:
            main_container = self.query_one("#transactions-table-main-container")
            transactions = self.query_one("#transactions-table")
            transactions.update(self.data_table_provider.create_panel(main_container.size.width))
            time.sleep(10)
