# erc20_token

- This explains how to mint/send/show ERC20 tokens on kovan testnet

- ERC20 Contract <https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/ERC20.sol>


## Install nodejs, npm, git
```
sudo apt install nodejs npm
sudo apt install git

sudo add-apt-repository ppa:ethereum/ethereum
sudo add-apt-repository ppa:ethereum/ethereum-dev
sudo apt update
sudo apt install solchereum/ethereum-dev
sudo apt update
sudo apt install solc
```


## Install brownie and ganache

```
sudo pip3 install eth-brownie
```

```
sudo npm install -g ganache-cli
```
or 
```
sudo npm install -g ganache
```


## Settings of ethereum kovan testnet

- Insert web3 infura project ID from infura <https://infura.io> into ***

```
export WEB3_INFURA_PROJECT_ID='***'
```


- Inset your private key from your metamask account into ***

```
export PRIVATE_KEY=***
```


## Get ETH of kovan testnet from faucet

- Install Metamask <https://metamask.io/>
  To do this, you can follow the instruction from ![this](MetaMask_HowToCreateAccount.pdf). (Thanks to Hikaru!)
- Then, get an account address
- Get some ETH from faucent (more than 0.004 ETH is recommended) <https://ethdrop.dev> or <https://gitter.im/kovan-testnet/faucet>


## git clone

```
git clone https://github.com/fujihalab/erc20_token.git
```


## Edit contract 

- Edit token name (default: FujihaLab Token) and symbol (default: FLT) in contracts/MyERC20Token.sol


## Test minting tokens using ganache

- Open 1st terminal, then run the following command

```
$ ganache-cli 
```

- Open 2nd terminal, then run the following command

```
brownie run scripts/mint_token.py

```


## Mint token

- Then, run the following command

```
brownie run scripts/mint_token.py --network kovan
```

The standard output goes like this:

```
Brownie v1.18.1 - Python development framework for Ethereum

Compiling contracts...
  Solc version: 0.8.13
  Optimizer: Enabled  Runs: 200
  EVM Version: Istanbul
Generating build data...
 - OpenZeppelin/openzeppelin-contracts@4.3.2/ERC20
 - OpenZeppelin/openzeppelin-contracts@4.3.2/IERC20
 - OpenZeppelin/openzeppelin-contracts@4.3.2/IERC20Metadata
 - OpenZeppelin/openzeppelin-contracts@4.3.2/Context
 - MyERC20Token

Erc20TokenProject is the active project.

Running 'scripts/mint_token.py::main'...
account: 0x3d5E61c1Bc6e882478ec3b6f814e7C95bEe7928a
Transaction sent: 0x7423851904ac9a15b5a7a16fa316e89315b25965f48fb34f0f5d4e3644892039
  Gas price: 2.500000007 gwei   Gas limit: 703000   Nonce: 6
  MyERC20Token.constructor confirmed   Block: 31509506   Gas used: 639091 (90.91%)
  MyERC20Token deployed at: 0x28E71A57454b0003632adc80279970925aDf96b2

```

- See Etherscan (Insert corresponding information into *)

<https://kovan.etherscan.io/address/*>

<https://kovan.etherscan.io/tx/*>

<https://kovan.etherscan.io/token/*>

- For example, 

<https://kovan.etherscan.io/address/0x3d5E61c1Bc6e882478ec3b6f814e7C95bEe7928a>
<https://kovan.etherscan.io/tx/0x7423851904ac9a15b5a7a16fa316e89315b25965f48fb34f0f5d4e3644892039>
<https://kovan.etherscan.io/token/0x28E71A57454b0003632adc80279970925aDf96b2>


## Send token

- Edit contract and recipient addresses in script/send_token.py 
- Edit the amount of tokens to send in script/send_token.py (default: 100 tokens)
- Then, run the following command

```
brownie run scripts/send_token.py --network kovan
```

The standard output goes like this:

```
Brownie v1.18.1 - Python development framework for Ethereum

Erc20TokenProject is the active project.

Running 'scripts/send_token.py::main'...
Transaction sent: 0x9bb39dbf10843b9c922c1b326a2487305ec9ce4ce0e67fc7dc0cc84078af3e6a
  Gas price: 2.500000007 gwei   Gas limit: 56756   Nonce: 7
  MyERC20Token.transfer confirmed   Block: 31509687   Gas used: 51597 (90.91%)

  MyERC20Token.transfer confirmed   Block: 31509687   Gas used: 51597 (90.91%)

```


## Show token status

- Edit contract and owner addresses in script/show_token_status.py 
- Then, run the following command

```
brownie run scripts/show_token_status.py --network kovan
```

The standard output goes like this:

```
Brownie v1.18.1 - Python development framework for Ethereum

Erc20TokenProject is the active project.

Running 'scripts/show_token_status.py::main'...
Token Name = FujihaLab Token
Token Symbol = FLT
Token Decimals = 18
Token Total Supply = 1000000000000000000000000
Token Balance = 999900000000000000000000

```


## Check token using Metamask

- Import tokens --> Insert token import address --> Add custom token --> Import tokens

<https://www.followchain.org/add-custom-token-metamask/>


