from brownie import Contract, GatekeeperOne, OpenGate
from scripts.helpful_scripts import *
from web3 import Web3

account = getAccount()
gate = Contract.from_abi(
    "GatekeeperOne", "0xfa9B1368602f73eCfbF71b5419d8Dee2e1890bBc", GatekeeperOne.abi
)

open = OpenGate.deploy({"from": account})
# open = OpenGate[-1]

tx = open.open({"from": account})
tx.wait(1)
print(gate.entrant())


def main():
    pass
