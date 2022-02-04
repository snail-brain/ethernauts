from brownie import Diddle
from scripts.helpful_scripts import *

account = getAccount()


def main():
    diddle = Diddle.deploy({"from": account})
    diddle.do_the_thing({"from": account})
