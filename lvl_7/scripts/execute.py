from os import kill
from brownie import kmsMyself
from scripts.helpful_scripts import *
from web3 import Web3

account = getAccount()
killer = kmsMyself.deploy({"from": account})


def main():
    tx = killer.deposit({"from": account, "value": Web3.toWei(0.0001, "ether")})
    tx.wait(1)
    killer.kill_me()
