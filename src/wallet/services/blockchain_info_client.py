import requests


class BlockchainInfoClient:

    def __init__(self, testnet: bool = False):
        if not testnet:
            self.url = "https://mempool.space/api"
        else:
            self.url = "https://mempool.space/testnet/api"

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
    app = BlockchainInfoClient(testnet=True)
    print(app.get_transactions("tb1qvr3m0d0f6hte7xjex7qufg7s2p4dh534sezqnp"))


