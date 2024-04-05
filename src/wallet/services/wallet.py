from bitcoinlib.wallets import Wallet, WalletError
from .blockchain_info_client import BlockchainInfoClient
from datetime import datetime

SATOSHI = 100_000_000


class Balance(object):
    total_received = 0
    total_sent = 0
    final_balance = 0
    total_txs = 0

    def __init__(self, total_received, total_sent, final_balance, total_txs):
        self.total_received = total_received
        self.total_sent = total_sent
        self.final_balance = final_balance
        self.total_txs = total_txs


class Transaction(object):
    tx_id = ""
    confirmations = 0
    time = 0
    value = 0.0

    def __init__(self, tx_id, confirmations, time, value):
        self.tx_id = tx_id
        self.confirmations = confirmations
        self.time = time
        self.value = value


class WalletService:

    def __init__(self, wallet_name, network):
        self.blockchain = BlockchainInfoClient(testnet=(network == "testnet"))
        try:
            self.wallet = Wallet.create(wallet_name, witness_type='segwit', network=network)
        except WalletError as e:
            self.wallet = Wallet(wallet_name)

    def get_address(self):
        return self.wallet.addresslist()[0]

    def get_balance_raw(self):
        response = self.blockchain.get_address_details(self.get_address())
        return response

    def get_balance(self) -> Balance:
        """ Returns the current balance of the wallet """
        response = self.blockchain.get_address_details(self.get_address())

        final_balance = response["chain_stats"]['funded_txo_sum'] - response["chain_stats"]['spent_txo_sum']

        if "error" in response:
            return Balance(0, 0, 0, 0)
        else:
            return Balance(
                response["chain_stats"]['funded_txo_sum'] / SATOSHI,
                response["chain_stats"]['spent_txo_sum'] / SATOSHI,
                final_balance / SATOSHI,
                response["chain_stats"]['tx_count'],
            )

    def get_transactions(self, limit) -> [Transaction]:
        """
        Returns all the transactions for the current address
        """
        block_height = self.blockchain.get_latest_block_height()
        txs = self.blockchain.get_transactions(self.get_address())
        transactions = []
        for transaction in txs:
            value = 0
            confirmations = 0
            for output in transaction["vout"]:
                # Only take into account the output that goes to this addressb
                if output["scriptpubkey_address"] == self.get_address():
                    value = value + output["value"]

            if transaction["status"]["confirmed"]:
                confirmations = block_height - transaction["status"]["block_height"] + 1

            transactions.append(Transaction(
                transaction["txid"],
                confirmations,
                "",
                str(value / SATOSHI)
            ))

            if len(transactions) == limit:
                break

        return transactions

    def send(self, to: str, amount: int) -> bool:
        """ Sends bitcoin to the destination address"""

        if to == self.get_address():
            return False

        if amount <= 0:
            return False

        self.wallet.send_to(to_address=to, amount=amount)
        return True
