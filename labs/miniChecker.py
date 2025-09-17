import requests
import json
from web3 import Web3, HTTPProvider

rpc = "your rpc"
api = "your api a scanner"
web3 = Web3(Web3.HTTPProvider(rpc))

response = requests.get(api)
if requests.get(api):
    print("successfully connected to network!")
else:
    print("error, again later please")
    
    
address = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984" # uniswap
data = response.json()
abi = json.loads(data['result'])

def data_address():
    contract = web3.eth.contract(address=address, abi=abi) 
    
    functions_library = {
        print(f"name - {contract.functions.name().call()}"),
        print(f"symbol - {contract.functions.symbol().call()}"),
        print(f"totalSupply - {contract.functions.totalSupply().call()}"),
        print(f"decimals - {contract.functions.decimals().call()}")
    }
data_address()
