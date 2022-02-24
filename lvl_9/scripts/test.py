from brownie import Contract, King
from scripts.helpful_scripts import *
from web3 import Web3

king = Contract.from_abi("King", "0x1562fdCabB4e8daFF5F3dDE341525c0438Bc3145", King.abi)
account = getAccount()


def main():
    print(Web3.fromWei(king.prize(), "ether"))
    print(king._king())
