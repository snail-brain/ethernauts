from web3 import Web3
from scripts.helpful_scripts import *


account = getAccount()


def main():
    deploy_bytes = "0x600a600c600039600a6000f3602a60805260206080f3"
    account.transfer(data=deploy_bytes)
