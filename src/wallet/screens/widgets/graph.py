import plotext as plt
from textual.widgets import Static
from rich.text import Text
from services import CoinbaseClient


class Graph(Static):

    def __init__(self) -> None:
        super().__init__()
        self.metric_instance = None
        self.coinbase_client = CoinbaseClient()

    def on_mount(self) -> None:
        self.render_graph(self.metric_instance)

    def on_resize(self) -> None:
        self.render_graph(self.metric_instance)

    def render_graph(self, metric_instance) -> None:
        self.metric_instance = metric_instance

        data = self.coinbase_client.get_historical_price()

        prices = data["Close"]
        dates = plt.datetime_to_string(data.index)

        plt.clf()
        plt.title("Bitcoin Daily Price")
        plt.xlabel("Date")
        plt.ylabel("Price")
        # plt.date_form("dd/mm/yyyy")
        plt.canvas_color((10, 14, 27))
        plt.axes_color((10, 14, 27))
        plt.ticks_color((133, 159, 213))
        plt.plotsize(self.size.width, self.size.height)

        plt.candlestick(dates, data)

        self.update(Text.from_ansi(plt.build()))
