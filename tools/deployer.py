from web3 import Web3, HTTPProvider
from solcx import compile_standard, install_solc, set_solc_version


""" WARNING:
    this code is designed to work with infura rpc node and sepolia testnet
    if you are using another node and testnet, changes may be required to make this code work!
"""

install_solc("0.8.29")
set_solc_version("0.8.29")

infura_url = "your api"
address_wallet = "your address wallet"
wallet_key = "private key your wallet"

w3 = Web3(Web3.HTTPProvider(infura_url))
if w3.is_connected():
    print(f"successfully connected to web3! {w3.is_connected()}")
else:
    print(f"you cant connected to web3, please again later!")

nonce = w3.eth.get_transaction_count(address_wallet)

with open ("StandardERC20.sol", "r") as file:
    source_codes = file.read()
    compiled_sol = compile_standard(
    {
            "language": "Solidity",
                "sources": 
            {"StandardERC20.sol": 
                {"content" : source_codes } 
            },
            "settings": { "outputSelection": { "*" : 
                { "*" : ["abi", "evm.bytecode"] } 
            } 
        }
    })


abi = compiled_sol["contracts"]["StandardERC20.sol"]["ERC20"]["abi"]
bytecode = compiled_sol["contracts"]["StandardERC20.sol"]["ERC20"]["evm"]["bytecode"]["object"]

contract = w3.eth.contract(bytecode=bytecode, abi=abi)
transaction = contract.constructor().build_transaction(
    {
        "chainId": 11155111,
        "gasPrice": w3.eth.gas_price,
        "from": address_wallet,
        "nonce": nonce
    })

sign_txn = w3.eth.account.sign_transaction(transaction, private_key=wallet_key)
txn_hash = w3.eth.send_raw_transaction(sign_txn.raw_transaction)
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

print(nonce)
print("successfully deploy contract!")
print(f"contract deploying...")
print(f"completed! contract deploy for address - {txn_receipt.contractAddress}")
