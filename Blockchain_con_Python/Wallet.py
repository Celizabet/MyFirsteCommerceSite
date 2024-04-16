from Crypto.PublicKey import RSA
from Transaction import Transaction 
from BlockchainUtils import BlockchainUtils 
from Crypto.Signature import PKCS1_v1_5

class Wallet():
    
    def __init__(self):
        self.key_pair = RSA.generate(2048)
    
    def sign(self, data):
        data_hash = BlockchainUtils.hash(data)
        signature_scheme_object = PKCS1_v1_5.new(self.key_pair)
        signature = signature_scheme_object.sign(data_hash)
        return signature.hex() 
    
    @staticmethod
    def signature_valid(data, signature, public_key_string):
        signature = bytes.fromhex(signature)
        data_hash = BlockchainUtils.hash(data)
        public_key = RSA.importKey(public_key_string)
        signature_scheme_object = PKCS1_v1_5.new(public_key)
        signature_valid = signature_scheme_object.verify(data_hash, signature)
        return signature_valid
    
    def public_key_string(self):
        public_key_string = self.key_pair.publickey().exportKey('PEM').decode("utf-8")
        return public_key_string
    
    def create_tx(self, receiver, amount, tx_type):
        transaction = Transaction(self.public_key_string(), receiver, amount, tx_type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction
    
    def create_block(self, txs, last_hash, block_count):
        block = Block(txs, last_hash, self.public_key_string(), block_count)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block