import re

pattern = r"function\s+(\w+)\s*\("

def search():
    with open("StandardERC20.sol") as file:
        content = file.read()
        re.findall(pattern, content, flags=re.I)
        words = re.findall(pattern, content)
        return content
        
rename = {
    "_owner": "_deployer",
    "owner": "_deployer",
    "mint": "_dropped",
    "burn": "_taked",
    "startTrading": "goSellBuy",
    "stopTrading": "stopSellBuy",
    "_statusTrading": "_checkTrade",
    "recipient": "receiver",
    "StoppedTrading": "unavailableTrade",
    "StartedTrading": "availableTrade",
    "account": "acc",
    "_balances": "_valueAcc",
    "_allowances": "_additions"
}


def renaming(content, rename):
    new_txt = content
    for old, new in rename.items():
        pattern = r'(?<!\w){}(?!\w)'.format(old)
        new_txt = re.sub(pattern, new, new_txt)
        with open("testContract.sol", "w") as file:
            data = new_txt
            file.write(data)
        print(new_txt)
            

        
contract_text = search()
renaming(contract_text, rename)
