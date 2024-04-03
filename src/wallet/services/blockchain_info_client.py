import requests


class BlockchainInfoClient:

    def __init__(self):
        self.url = "https://mempool.space/api"

    def get_latest_block_height(self) -> int:
        endpoint = self.url + "/blocks/tip/height"
        r = requests.get(url=endpoint)
        return int(r.text)

    def get_latest_block_hash(self) -> str:
        endpoint = self.url + "/blocks/tip/hash"
        r = requests.get(url=endpoint)
        return r.text

    def get_latest_block_info(self):
        endpoint = self.url + "/block/" + self.get_latest_block_hash()
        r = requests.get(url=endpoint)
        return r.json()

    def get_address_details(self, address):
        endpoint = self.url + "/address/" + address
        r = requests.get(url=endpoint)
        return r.json()

    def get_transactions(self, address):
        endpoint = self.url + "/address/" + address + "/txs"
        r = requests.get(url=endpoint)
        return r.json()


if __name__ == '__main__':
    app = BlockchainInfoClient()
    result = app.get_latest_block_height()
    print(result + 1)
    #print(app.get_latest_block_info())
    #print(app.get_address_details("bc1q7cyrfmck2ffu2ud3rn5l5a8yv6f0chkp0zpemf"))
    print(app.get_transactions("bc1q7cyrfmck2ffu2ud3rn5l5a8yv6f0chkp0zpemf"))

