from textual.app import ComposeResult
from textual.widgets import Label, Input, Button
from textual.containers import Container, Vertical, Horizontal, Grid
from textual.screen import ModalScreen
from .modal_bar import ModalBar
from rich.text import Text
from services import WalletService
import qrcode
import io


class ReceiveModal(ModalScreen[None]):
    BINDINGS = [("escape", "pop_screen")]

    DEFAULT_CSS = """
    ReceiveModal {
        align: center middle;
    }

    #receive-screen-container {
        width: auto;
        height: auto;
        max-width: 70%;
        max-height: 90%;
        background: $panel;
        align: center middle;
        padding: 1 2
    }

    #receive-modal-buttons {
        align: center middle;
        height: 5;
    }
    
    #qr-code-display {
        align: center middle;
    }
    
    #wallet-address {
        align: center middle;
        height: 3;
    }
    """

    def __init__(self):
        super().__init__()
        self.wallet_service = WalletService("my_wallet", "testnet")
        self.address = self.wallet_service.get_address()

    def compose(self) -> ComposeResult:
        with Container(id="receive-screen-container"):
            yield ModalBar("Receive Bitcoin ...")
            yield Horizontal(
                Label(Text.from_ansi(self.generate_qr_code(self.address))),
                id="qr-code-display"
            )
            yield Horizontal(
                Label(self.address),
                id="wallet-address"
            )
            yield Horizontal(
                Button("Send", id="receive-confirm", variant="success"),
                Button("Cancel", id="receive-cancel", variant="error"),
                id="receive-modal-buttons"
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """ Event handler called when a button is pressed. """

        if event.button.id == "receive-cancel":
            self.app.pop_screen()
        elif event.button.id == "receive-confirm":
            self.app.pop_screen()

    def generate_qr_code(self, text) -> str:
        qr = qrcode.QRCode()
        qr.add_data(text)
        f = io.StringIO()
        qr.print_ascii(out=f)
        f.seek(0)
        return f.read()
