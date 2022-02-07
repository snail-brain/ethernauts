pragma solidity ^0.6.0;

contract kmsMyself {
    uint256 balance = 0;
    address owner;

    constructor() public {
        owner = msg.sender;
    }

    function deposit() external payable {
        balance += msg.value;
    }

    function kill_me() public {
        if (msg.sender == owner) {
            selfdestruct(0xece72EA260CEBc47d540c578515F30304745eE4f);
        }
    }
}
