from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from textual.screen import ModalScreen


class WelcomeModal(ModalScreen[None]):
    BINDINGS = [("escape", "pop_screen")]

    DEFAULT_CSS = """
    WelcomeModal {
        align: center middle;
    }

    #welcome-screen-container {
        width: auto;
        height: auto;
        max-width: 70%;
        max-height: 70%;
        background: $panel;
        align: center middle;
        padding: 2 4
    }
    """

    def compose(self) -> ComposeResult:
        with Container(id="welcome-screen-container"):
            yield Label("BitcoinWallet app v0.0.1 ALPHA")
            yield Label("Please use at your own risk")
            yield Label(" ... ")
            yield Label("Press ESC to continue.")
