from textual.app import ComposeResult
from textual.widgets import Static, Label
from textual.containers import Vertical, Container, Center
from textual.widgets import DataTable
from rich.table import Table

class TransactionDetails:

    def create_panel(self) -> Table:
        transactions_table = Table(title="Transactions")

        columns = ("Type", "Date", "Hash", "Amount", "Confirmations", "Link")
        transactions_table.add_column("Type")
        transactions_table.add_column("Date")
        transactions_table.add_column("Hash")
        transactions_table.add_column("Amount", style="green")
        transactions_table.add_column("Confirmations")
        transactions_table.add_column("Link")

        transactions_table.add_row("Incoming", "01/02/2021", "86371ccb33282ffd780b85e3617753b948dabd4fa19a2692f3ac1217c184b000", "1.09887653", "1", "")
        transactions_table.add_row("Incoming", "01/02/2021", "7b07297f16bc71c2e2f80ab7dd0e9a99fe8ab54c5a3683d0c582b0dd6a155842", "1.09887652", "1", "")
        transactions_table.add_row("Incoming", "01/02/2021", "86371ccb33282ffd780b85e3617753b948dabd4fa19a2692f3ac1217c184b000", "1.09887651", "1", "")
        transactions_table.add_row("Incoming", "01/02/2021", "7b07297f16bc71c2e2f80ab7dd0e9a99fe8ab54c5a3683d0c582b0dd6a155842", "1.09887650", "1", "")
        transactions_table.add_row("Incoming", "01/02/2021", "86371ccb33282ffd780b85e3617753b948dabd4fa19a2692f3ac1217c184b000", "1.44553905", "1", "")
        transactions_table.add_row("Incoming", "01/02/2021", "7b07297f16bc71c2e2f80ab7dd0e9a99fe8ab54c5a3683d0c582b0dd6a155842", "1.09887654", "1", "")
        transactions_table.add_row("Incoming", "01/02/2021", "86371ccb33282ffd780b85e3617753b948dabd4fa19a2692f3ac1217c184b000", "1.09887655", "1", "")
        transactions_table.add_row("Outgoing", "01/02/2021", "86371ccb33282ffd780b85e3617753b948dabd4fa19a2692f3ac1217c184b000", "1.09887656", "1", "")

        return transactions_table


class RecentTransactions(Static):

    def __init__(self):
        super().__init__()
        self.data_table_provider = TransactionDetails()

    def compose(self) -> ComposeResult:
        yield Container(
            Center(
                Static(id="transactions-table")
            )
        )

    def on_mount(self) -> None:
        transactions = self.query_one("#transactions-table")
        transactions.update(self.data_table_provider.create_panel())
