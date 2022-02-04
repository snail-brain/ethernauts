from brownie import FlipGuess
from scripts.helpful_scripts import *

account = getAccount()


def main():
    FlipGuess.deploy({"from": account})
