import time

from textual import work
from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.containers import Container, Center, Horizontal
from rich.table import Table
from rich.style import Style
from screens.modals import SendModal, ReceiveModal
from services import WalletService


class Balance(Static):
    DEFAULT_CSS = """
        Balance {
            align: center middle;
            width: 100%
        }

        #buttons-send-receive {
            align: center middle;
        }
    """

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
            ),
            Center(
                Horizontal(
                    Button("Send", variant="error", id="send-button"),
                    Button("Receive", variant="success", id="receive-button"),
                    id="buttons-send-receive"
                )
            )
        )

    def on_mount(self) -> None:
        self.refresh_balance()

    @work(exclusive=True, thread=True)
    def refresh_balance(self) -> None:
        """ Refresh the table every 10 seconds """
        while True:
            balance_table = self.query_one("#balance-table")
            balance_table.update(self.create_table())
            time.sleep(10)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """ Event handler called when a button is pressed. """
        if event.button.id == "send-button":
            self.app.push_screen(SendModal())
        elif event.button.id == "receive-button":
            self.app.push_screen(ReceiveModal())

    def create_table(self) -> Table:
        """ Create the balance table. """
        balance = self.wallet_service.get_balance()
        table_title_style = Style(color="#bbc8e8", bold=True)
        table_information = Table(show_header=False,
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
