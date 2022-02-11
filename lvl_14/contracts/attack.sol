pragma solidity ^0.6.0;

import "./default.sol";
import "./test.sol";

contract OpenGate {
    address public me;
    bytes8 public key;
    uint64 public overload = uint64(0) - 1;
    GatekeeperTwo gate =
        GatekeeperTwo(0xB83d8245e2Aeceb7518Af9BE0Cea9C39217AA444);

    constructor() public {
        me = address(this);
        uint64 poop = uint64(bytes8(keccak256(abi.encodePacked(me))));
        key = bytes8(poop ^ overload);
        gate.enter(key);
    }
}
