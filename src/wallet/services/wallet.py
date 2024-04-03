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
        self.blockchain = BlockchainInfoClient()
        try:
            self.wallet = Wallet.create(wallet_name, witness_type='segwit', network=network)
        except WalletError as e:
            self.wallet = Wallet(wallet_name)

    def get_address(self):
        # return self.wallet.addresslist()[0] TODO uncomment this to use real data for now let's use a real adddress with real data
        return "bc1q7cyrfmck2ffu2ud3rn5l5a8yv6f0chkp0zpemf"

    def get_balance_raw(self):
        response = self.blockchain.get_address_details(self.get_address())
        return response

    def get_balance(self) -> Balance:
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

    def get_transactions(self) -> [Transaction]:
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
                value = value + output["value"]

            if transaction["status"]["confirmed"]:
                confirmations = block_height - transaction["status"]["block_height"] + 1

            transactions.append(Transaction(
                transaction["txid"],
                confirmations,
                "",
                str(value / SATOSHI)
            ))

            if len(transactions) == 20:
                break

        return transactions
