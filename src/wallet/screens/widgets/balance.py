from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Container, Center
from rich.table import Table
from rich.style import Style
from services import WalletService, Balance


class Balance(Static):

    def __init__(self):
        super().__init__()

        self.wallet_service = WalletService("my_wallet", "testnet")
        self.address = self.wallet_service.get_address()
        self.available = "0"
        self.pending = "0"
        self.total = "0"

    def compose(self) -> ComposeResult:
        yield Container(
            Center(
                Static(id="balance-table")
            )
        )

    def on_mount(self) -> None:
        balance_table = self.query_one("#balance-table")
        balance_table.update(self.create_table())

    def create_table(self) -> Table:
        balance = self.wallet_service.get_balance()
        table_title_style = Style(color="#bbc8e8", bold=True)
        table_information = Table(show_header=False,
                                  box=None,
                                  title="Balance Information",
                                  title_style=table_title_style)

        table_information.add_column(justify="left", style="cyan")
        table_information.add_column(min_width=25, no_wrap=True, justify="right")
        table_information.add_row("[label]Address", f"{self.address}")
        table_information.add_row("[label]Available", f"{balance.total_received} BTC")
        table_information.add_row("[label]Total Sent", f"{balance.total_sent} BTC")
        table_information.add_row("[label]Final Balance", f"{balance.final_balance} BTC")
        table_information.add_row("[label]Total txs", f"{balance.total_txs}")

        return table_information
