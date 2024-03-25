from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Container
from textual.screen import ModalScreen


class HelpScreen(ModalScreen[None]):
    BINDINGS = [("escape", "pop_screen")]

    DEFAULT_CSS = """
    HelpScreen {
        align: center middle;
    }

    #help-screen-container {
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
        with Container(id="help-screen-container"):
            yield Label("BitcoinWallet app v0.0.1 ALPHA")
            yield Label("Created by nanexcode (hartmanmario at gmail dot com)")
            yield Label("")
            yield Label("Press ESC to exit.")
