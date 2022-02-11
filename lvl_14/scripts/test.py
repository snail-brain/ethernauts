from brownie import Contract, OpenGate, GatekeeperTwo
from scripts.helpful_scripts import *

account = getAccount()

gate = Contract.from_abi(
    "GatekeeperTwo", "0xB83d8245e2Aeceb7518Af9BE0Cea9C39217AA444", GatekeeperTwo.abi
)


def main():
    attacker = OpenGate.deploy({"from": account})
    print(gate.entrant())
