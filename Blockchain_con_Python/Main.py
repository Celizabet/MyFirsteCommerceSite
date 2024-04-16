from BlockchainUtils import BlockchainUtils
from Blockchain import Blockchain
from TransactionPool import TransactionPool
import pprint

blockchain = Blockchain()
pool = TransactionPool()

def tx_in_pool(tx):
    """Add tx to the pool"""
    if not pool.tx_exists(tx):
        pool.add_tx(tx)


def block_creation(wallet):
    """Create a block with the tx in the pool"""
    last_hash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    block_count = blockchain.blocks[-1].block_count + 1
    block = wallet.create_block(pool.transactions, last_hash, block_count)
    
    return block


def blockchain_cration(block):
    """Create a blockchain, add block to the bc and cleans the pool"""
    if not blockchain.last_block_hash_valid(block):
        print("last block hash is not valid")
    
    if not blockchain.block_count_valid(block):
        print("block count is not valid")
    
    if blockchain.last_block_hash_valid(block) and blockchain.block_count_valid(block):
        blockchain.add_block(block)
    
    pool.remove_from_pool(block.txs)

    pprint.pprint(blockchain.to_json())