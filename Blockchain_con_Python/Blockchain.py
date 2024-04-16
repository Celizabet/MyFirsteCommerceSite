from BlockchainUtils import BlockchainUtils
from Block import Block

class Blockchain():
    
    def __init__(self):
        self.blocks = [Block.genesis()]
        self.account_model = AccountModel()
    
    def add_block(self, block):
        self.blocks.append(block)
        
    def to_json(self):
        data = {}
        json_blocks = []
        for block in self.blocks:
            json_blocks.append(block.to_json())
        data["blocks"] = json_blocks
        return data
    
    def block_count_valid(self, block):
        if self.blocks[-1].block_count == block.block_count -1:
            return True
        else:
            return False
        
    def last_block_hash_valid(self, block):
        latest_blockchain_block_hash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        if latest_blockchain_block_hash == block.last_hash:
            return True
        else: 
            return False
    
    def get_covered_txs_set(self, txs):
        covered_txs = []
        for tx in txs:
            if self.tx_covered(tx):
                covered_txs.append(tx)
            else:
                print("tx amount can not be covered")
        return covered_txs
    
    def tx_covered(self, tx):
        if tx.tx_type == "EXCHANGE":
            return True
        sender_balance = self.account_model.get_balance(tx.sender_public_key)
        if sender_balance >= tx.amount:
            return True
        else:
            return False
        
    def execute_txs(self, txs):
        for tx in txs:
            self.execute_tx(tx)
            
    def execute_tx(self, tx):
        sender = tx.sender_public_key
        receiver = tx.receiver_public_key
        amount = tx.amount
        self.account_model.update_balance(sender, -amount)
        self.account_model.update_balance(receiver, amount)