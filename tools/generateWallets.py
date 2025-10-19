from web3 import Web3
import sqlite3
import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.info

web3 = Web3()

connect = sqlite3.connect('wallets.db')
cursor = connect.cursor()

cursor.execute('create table if not exists Wallets (address TEXT, key TEXT)')

def save(address, key):
    cursor.execute('insert into Wallets (address, key) values (?, ?)' , (address, key))
    connect.commit()
    
def generate():
    for _ in range(50):
        account = web3.eth.account.create()
        address = account.address
        key = account.key.hex()
        save(address, key)
        
        log(f'Address - {address} Private Key - {key}')

generate()
