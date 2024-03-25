from textual.app import ComposeResult
from textual.widgets import Static, Label, Input
from textual.containers import Horizontal


class LabelledInput(Static):
    DEFAULT_CSS = """
    LabelledInput {
        align: center middle;
    }
    """

    def __init__(self, label):
        super().__init__()
        self.label = label

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Label(f"{self.label}:"),
            Input()
        )
