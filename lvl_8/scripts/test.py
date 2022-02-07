from scripts.helpful_scripts import *
from brownie import chain, Contract, Vault
from web3 import Web3

w3 = Web3(
    Web3.HTTPProvider(
        "https://eth-rinkeby.alchemyapi.io/v2/e2HrX3zIlZIa3nI7nhUILDcL3L2WWldD"
    )
)
account = getAccount()

vault = Contract.from_abi(
    "Vault", "0x7fAfBF2b619c8FDB44097494f25abE67AaC4cf00", Vault.abi
)


def main():
    print(w3.eth.get_storage_at(vault.address, 1))
