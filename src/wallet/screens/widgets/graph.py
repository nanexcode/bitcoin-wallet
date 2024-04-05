import time

import plotext as plt
from textual import work
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

    async def on_resize(self) -> None:
        self.render_graph(self.metric_instance)

    @work(exclusive=True, thread=True)
    def render_graph(self, metric_instance) -> None:
        while True:
            self.metric_instance = metric_instance

            data = self.coinbase_client.get_historical_price()
            dates = plt.datetime_to_string(data.index, output_form="d/m/Y H:M:S")

            plt.clf()
            plt.title("Bitcoin Daily Price")
            plt.xlabel("Date")
            plt.ylabel("Price")
            plt.canvas_color((10, 14, 27))
            plt.axes_color((10, 14, 27))
            plt.ticks_color((133, 159, 213))
            plt.plotsize(self.size.width, self.size.height)
            plt.date_form("d/m/Y H:M:S")

            plt.candlestick(dates, data)

            self.update(Text.from_ansi(plt.build()))
            time.sleep(60)