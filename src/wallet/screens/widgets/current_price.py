from textual.app import ComposeResult
from textual.widgets import Static, Label, Sparkline
from textual.containers import Vertical
from services import CoinbaseClient

import random
from statistics import mean
from math import sin
random.seed(73)
data = [abs(sin(x / 3.14)) for x in range(0, 360 * 6, 20)]


class CurrentPrice(Static):
    DEFAULT_CSS = """
    CurrentPrice {
        align: left top;
        padding: 1;
    }
    
    Sparkline {
        align: center top;
        width: 100%;
        height: 20;
        margin: 2;
    }
    
    #price_data > .sparkline--max-color {
        color: $success;
    }
    #price_data > .sparkline--min-color {
        color: $warning;
    }
    """

    def __init__(self):
        super().__init__()
        self.price_service = CoinbaseClient()

    def compose(self) -> ComposeResult:
        yield Label("", id="price-label")

    async def on_mount(self):
        await self.update_price()
        self.set_interval(20.0, self.update_price)

    async def update_price(self):
        try:
            price = self.query_one("#price-label")
            price.update(f"Current price {self.price_service.get_bitcoin_price()} USD")
        except:
            print("err")
