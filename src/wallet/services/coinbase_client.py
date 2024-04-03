from datetime import date
from dateutil import relativedelta
import requests
import yfinance as yf


class CoinbaseClient:

    def __init__(self):
        self.url = "https://api.exchange.coinbase.com/products/"

    def get_price(self, pair):
        """
        Returns the current price for a given pair.
        """
        endpoint = self.url + pair.replace("/", "-") + "/book"
        r = requests.get(url=endpoint)
        return r.json()

    def get_bitcoin_price(self):
        """
        Returns current BTC/USD price
        """
        response = self.get_price("BTC/USD")
        return response["asks"][0][0]

    def get_products(self):
        """
        Returns all the available products in the API.
        Since this is a bitcoin wallet we care about bitcoin price only
        """
        r = requests.get(url=self.url)
        data = r.json()
        for product in data:
            print(product['id'])

    def get_historical_price(self):
        """
        Returns historical data from yfinance api.
        Thr response has the following data

        Date Open High Low Close ... Volume
        """

        today = date.today()
        month = today - relativedelta.relativedelta(months=1)
        data = yf.download('BTC-USD', start=month, end=today)
        return data


if __name__ == '__main__':
    service = CoinbaseClient()
    print(service.get_historical_price())
