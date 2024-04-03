import os

from textual.app import App, ComposeResult
from textual.binding import Binding
from screens.modals import HelpScreen, WelcomeModal
from screens import MainScreen
from screens.widgets import TopBar
from rich.theme import Theme


class Wallet(App):
    """A class representing a trading application."""

    TITLE = "Bitcoin Wallet"
    #CSS_PATH = "wallet.css"

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="question_mark", action="get_help", description="Show help screen", key_display="?"),
    ]

    def __init__(self):
        super().__init__()

        theme = Theme(
            {
                "white": "#e9e9e9",
                "green": "#54efae",
                "yellow": "#f6ff8f",
                "dark_yellow": "#cad45f",
                "red": "#fd8383",
                "purple": "#b565f3",
                "dark_gray": "#969aad",
                "highlight": "#91abec",
                "label": "#c5c7d2",
                "b label": "b #c5c7d2",
                "light_blue": "#bbc8e8",
                "b white": "b #e9e9e9",
                "b highlight": "b #91abec",
                "b red": "b #fd8383",
                "b light_blue": "b #bbc8e8",
                "panel_border": "#6171a6",
                "table_border": "#333f62",
            }
        )
        #self.console.push_theme(theme)
        self.console.set_window_title(self.TITLE)

    def compose(self) -> ComposeResult:
        """Create the app layout and widgets."""
        yield TopBar(app_version="0.0.1 alpha")
        yield MainScreen()

    def on_mount(self) -> None:
        self.push_screen(WelcomeModal())

    def action_get_help(self) -> None:
        self.push_screen(HelpScreen())


def main():
    # Set environment variables so Textual can use all the pretty colors
    os.environ["TERM"] = "xterm-256color"
    os.environ["COLORTERM"] = "truecolor"
    app = Wallet()
    app.run()


if __name__ == "__main__":
    main()
