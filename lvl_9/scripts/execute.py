from brownie import King, BadKing, Contract
from scripts.helpful_scripts import *
from web3 import Web3

account = getAccount()

king = Contract.from_abi("King", "0x4047A8083f3e637C795d6a649087CDE96a8d092e", King.abi)


def main():
    badking = BadKing.deploy({"from": account, "value": Web3.toWei(0.0015, "ether")})
    badking = BadKing[-1]
    tx = badking.becomeKing({"from": account})
    tx.wait(1)
    print(Web3.fromWei(king.prize(), "ether"))


# Well fuck this one. I've even looked up the answer but it doesn't want to work for some reason, on to
# the next one
