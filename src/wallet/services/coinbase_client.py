import requests


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


if __name__ == '__main__':
    service = CoinbaseClient()
    print("Bitcoin price " + str(service.get_bitcoin_price()))
