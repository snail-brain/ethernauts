from brownie import FlipGuess, CoinFlip, Contract
from scripts.helpful_scripts import *

account = getAccount()
guesser = FlipGuess[-1]
default = Contract.from_abi(
    "CoinFlip", "0x605A0c3018aEF2145F7c427581CaCD8dBf37Cc16", FlipGuess.abi
)


def main():
    tx = guesser.guess({"from": account})
    tx.wait(1)
