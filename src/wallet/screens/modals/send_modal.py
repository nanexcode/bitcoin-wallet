from textual.app import ComposeResult
from textual.widgets import Label, Input, Button
from textual.containers import Container, Vertical, Horizontal, Grid
from textual.screen import ModalScreen
from .modal_bar import ModalBar
from services import WalletService

class SendModal(ModalScreen[None]):
    BINDINGS = [("escape", "pop_screen")]

    DEFAULT_CSS = """
    SendModal {
        align: center middle;
    }
    
    Grid {
        grid-size: 2 2;
    }

    #send-screen-container {
        width: auto;
        height: auto;
        max-width: 70%;
        max-height: 70%;
        background: $panel;
        align: center middle;
        padding: 2 4
    }
    
    #send-modal-buttons {
        align: center middle;
    }
    """

    def __init__(self):
        super().__init__()
        self.wallet_service = WalletService("my_wallet", "testnet")
        self.to_input = Input()
        self.amount_input = Input()

    def compose(self) -> ComposeResult:
        with Container(id="send-screen-container"):
            yield ModalBar("Send Bitcoin ...")
            yield Grid(
                Label("To: "),
                self.to_input,
                Label("Amount: "),
                self.amount_input
            )
            yield Horizontal(
                Button("Send", id="send-confirm", variant="success"),
                Button("Cancel", id="send-cancel", variant="error"),
                id="send-modal-buttons"
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """ Event handler called when a button is pressed. """
        if event.button.id == "send-cancel":
            self.app.pop_screen()
        elif event.button.id == "send-confirm":
            result = self.wallet_service.send(self.to_input.value, int(self.amount_input.value))
            if result:
                self.app.notify("Transaction sent successfully!")
            else:
                self.app.notify("Transaction failed.")
            self.app.pop_screen()
