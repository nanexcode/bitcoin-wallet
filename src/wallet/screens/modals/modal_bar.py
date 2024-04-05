from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Label


class ModalBar(Container):
    DEFAULT_CSS = """
    ModalBar {
        dock: top;
        background: #192036;
        height: 1;
        layout: horizontal;
    }
    #modalbar_title {
        width: 85%;
        content-align: left middle;
    }
    """

    def __init__(self, title=""):
        super().__init__()
        self.modal_bar_title = Label(title, id="modalbar_title")

    def compose(self) -> ComposeResult:
        yield self.modal_bar_title
