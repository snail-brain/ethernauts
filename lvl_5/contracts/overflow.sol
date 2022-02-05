pragma solidity 0.4.24;

// Testing Uint256 underflow and overflow in Solidity

contract UintWrapping {
    uint256 public zero = 0;
    uint256 public max = 2**256 - 1;

    // zero will end up at 2**256-1
    function zeroMinus1() public view returns (uint256) {
        return zero -= 1;
    }

    // max will end up at 0
    function maxPlus1() public view returns (uint256) {
        return max += 1;
    }
}
