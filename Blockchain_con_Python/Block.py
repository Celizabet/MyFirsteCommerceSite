import time
from copy import deepcopy

class Block():
    
    def __init__(self, txs, last_hash, forger, block_count):
        self.block_count = block_count
        self.txs = txs
        self.last_hash = last_hash
        self.forger = forger
        self.block_count = block_count
        self.timestamp = time.time()
        self.forger = forger
        self.signature = ""
 
    @staticmethod
    def genesis():
        genesis_block = Block([], "genesis_hash", "genesis", 0)
        genesis_block.timestamp = 0
        return genesis_block
    
    def to_json(self):
        data = {}
        data["blockCount"] = self.block_count
        data["lastHash"] = self.last_hash
        data["signature"] = self.signature
        data["forger"] = self.forger
        data["timestamp"] = self.timestamp
        
        json_txs = []
        for tx in self.txs:
            json_txs.append(tx.to_json())
        data["txs"] = json_txs
        return data
    
    def payload(self):
        json_representation = deepcopy(self.to_json())
        json_representation["signature"] = ""     
        return json_representation
    
    def sign(self, signature):
        self.signature = signature