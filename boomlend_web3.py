from web3 import Web3
from typing import Optional
from hexbytes import HexBytes
import json

rpc = 'https://polygon.llamarpc.com'
web3 = Web3(Web3.HTTPProvider(rpc))
web3.eth.account.enable_unaudited_hdwallet_features()
ABI = json.loads('''[{"inputs":[{"internalType":"address","name":"_tokenInstance","type":"address"},{"internalType":"uint256","name":"_tokenAmount","type":"uint256"},{"internalType":"uint256","name":"_waitTime","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"allowedToWithdraw","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getWithdrawableAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"requestTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_tokenAmount","type":"uint256"}],"name":"setTokenAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_waitTime","type":"uint256"}],"name":"setWaitTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"tokenAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"tokenInstance","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"waitTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_address","type":"address"}],"name":"withdrawTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]''')
contract_address = '0x3a1F862D8323138F14494f9Fb50c537906b12B81'
seed = 'seed.txt'

def boomland(seed1):
  with open(seed1, 'r', encoding='utf-8') as file:
    rows_list = list(map(str.rstrip, file.readlines()))
  for i in range(len(rows_list)):
    seed = rows_list[i]
    try:
        account = web3.eth.account.from_mnemonic(seed)
        private_key = web3.to_hex(account._private_key)
        address = account.address
        checksum_address = Web3.to_checksum_address(address)
        dict_transaction = {
            'chainId': web3.eth.chain_id,
            'from': address,
            'gasPrice': web3.eth.gas_price,
            'nonce': web3.eth.get_transaction_count(address),
            'gas': 210_000
        }
        contractXDXD = web3.eth.contract(contract_address, abi=ABI)
        transaction = contractXDXD.functions.requestTokens().build_transaction(dict_transaction)
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print(f'Token request: {txn_hash.hex()}')
    except ValueError:
        continue

boomland(seed)