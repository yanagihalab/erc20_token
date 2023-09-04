from brownie import accounts, config, Contract, MyERC20Token
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    erc20_address = "0x28E71A57454b0003632adc80279970925aDf96b2" # TO EDIT: Contract address
    owner = "0x3d5E61c1Bc6e882478ec3b6f814e7C95bEe7928a" # TO EDIT: Owner address

    # This will be how many tokens to send in WEI
    erc20 = Contract.from_abi("Send ERC20 Token", erc20_address, abi=MyERC20Token.abi)
    # get token basic definitions
    print("Token Name = {}".format(erc20.name()))
    print("Token Symbol = {}".format(erc20.symbol()))
    print("Token Decimals = {}".format(erc20.decimals()))
    print("Token Total Supply = {}".format(erc20.totalSupply()))
    print("Token Balance = {}".format(erc20.balanceOf(owner)))
