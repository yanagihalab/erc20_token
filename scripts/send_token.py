from brownie import accounts, config, Contract, MyERC20Token
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    erc20_address = "0x28E71A57454b0003632adc80279970925aDf96b2" # TO EDIT: Contract address
    recipient = "0x754bf4F82D125436168F6e45A78cfe7831d9358C" # TO EDIT: Recipient address

    # This will be how many tokens to send in WEI
    amount = 100 * (10**18)  # TO EDIT: Send 100 tokens (decimals=18) to the recipient
    erc20 = Contract.from_abi("Send ERC20 Token", erc20_address, abi=MyERC20Token.abi)
    tx = erc20.transfer(recipient, amount, {"from": account})
    tx.wait(1)
