pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyERC20Token is ERC20 {
    constructor() public ERC20("FujihaLab Token", "FLT") { // TO EDIT: Token name and symbol 
        _mint(msg.sender, 1*(10**6)*(10**18)); // amout:10**6, decimal:18
    }
}
