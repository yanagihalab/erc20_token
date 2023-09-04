from brownie import accounts, config, MyERC20Token
from scripts.helpful_scripts import get_account

def main():
  account = get_account()
  print('account:', account)
  erc20 = MyERC20Token.deploy({"from": account})
