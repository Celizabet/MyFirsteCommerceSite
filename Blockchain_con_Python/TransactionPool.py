class TransactionPool():
    
    def __init__(self):
        self.transactions = []
        
    def add_tx(self, tx):
        self.transactions.append(tx)
    
    def tx_exists(self, tx):
        for pool_tx in self.transactions:
            if pool_tx.equals(tx):
                return True
        return False
    
    def remove_from_pool(self, txs):
        new_pool_txs = []
        for pool_tx in self.transactions:
            insert = True
            for tx in txs:
                if pool_tx.equals(tx):
                    insert = False
            if insert:
                new_pool_txs.append(pool_tx)
        self.transactions = new_pool_txs