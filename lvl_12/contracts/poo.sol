pragma solidity ^0.6.0;

import "./default.sol";

contract Lockpick {
    Privacy privacy = Privacy(0xa3d265248C22FF5df0621742A5d41AdFe317121B);

    function pick_lock(bytes32 _data) public {
        bytes16 data = bytes16(_data);
        privacy.unlock(data);
    }
}
