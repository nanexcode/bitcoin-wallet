import requests

url = "https://api.exchange.coinbase.com/products/"

class CryptoPriceService:

    def get_price(self, pair):
        endpoint = url + pair.replace("/", "-") + "/book"
        r = requests.get(url = endpoint)
        return r.json()
    
    def get_products(self):
        endpoint = "https://api.exchange.coinbase.com/products"
        r = requests.get(url = endpoint)
        data = r.json()
        for product in data:
            print(product['id'])
    


if __name__ == '__main__':
    service = CryptoPriceService()
    products = service.get_products()
    price = CryptoPriceService().get_price("btc/usd")
    print(price)
    print(price['bids'][0][0])
    print(price['asks'][0][0])
