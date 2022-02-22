pragma solidity ^0.6.0;

contract Attack {
    receive() external payable {
        assert(false);
    }
}
