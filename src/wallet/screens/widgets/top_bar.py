from textual.app import ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Label


class TopBar(Container):

    def __init__(self, app_version="", help="press [b highlight]q[/b highlight] to return"):
        super().__init__()
        self.topbar_title = Label(f" [b light_blue]Octo Wallet[/b light_blue] :octopus: [light_blue]v{app_version}", id="topbar_title")
        self.topbar_help = Label(help, id="topbar_help")

    def compose(self) -> ComposeResult:
        yield self.topbar_title
        yield self.topbar_help
