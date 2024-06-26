from textual.app import ComposeResult
from textual.widgets import Static
from .widgets import RecentTransactions
from .widgets import Balance
from .widgets import Graph


class MainScreen(Static):
    DEFAULT_CSS = """
    MainScreen {
        layout: grid;
        grid-size: 3;
    }
    
    Graph {
        column-span: 3;
        tint: magenta 1%;
        height: 20;
        border: panel
    }
    
    Balance {
        border: double #a5b8e7;
    }
    
    RecentTransactions {
        column-span: 2;
        width: 100%;
        border: double #a5b8e7;
    }
    """

    def compose(self) -> ComposeResult:
        #yield Graph()
        yield Balance()
        yield RecentTransactions()


