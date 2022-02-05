from brownie import UintWrapping, Attacker
from scripts.helpful_scripts import *

account = getAccount()


def main():
    Attacker.deploy({"from": account})
