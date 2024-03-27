import requests


class BlockchainInfoClient:

    def __init__(self):
        self.url = "https://blockchain.info"

    def get_latest_block_info(self):
        endpoint = self.url + "/latestblock"
        r = requests.get(url=endpoint)
        return r.json()

    def get_address_details(self, address):
        endpoint = self.url + "/rawaddr/" + address
        r = requests.get(url=endpoint)
        return r.json()


if __name__ == '__main__':
    app = BlockchainInfoClient()
    print(app.get_latest_block_info())
    print(app.get_address_details("bc1q7cyrfmck2ffu2ud3rn5l5a8yv6f0chkpzpemf"))

