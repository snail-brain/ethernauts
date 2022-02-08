from brownie import Contract, King
from scripts.helpful_scripts import *
from web3 import Web3

king = Contract.from_abi("King", "0xEc94491b2A0BaBd24637386E768718f900801291", King.abi)
account = getAccount()


def main():
    print(Web3.fromWei(king.prize(), "ether"))
    print(king._king())
