from brownie import SimpleToken, Contract
from scripts.helpful_scripts import *

account = getAccount()

token = Contract.from_abi(
    "SimpleToken", "0x594000a709E0C7823E68516b17dE57b14043Ebd7", SimpleToken.abi
)
dummie = "0x0EB8e4771ABA41B70d0cb6770e04086E5aee5aB2"


def main():
    tx = token.destroy(dummie, {"from": account})
    tx.wait(1)
