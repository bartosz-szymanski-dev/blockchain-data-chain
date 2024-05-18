import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.proof = proof
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(f'{self.index}{self.previous_hash}{self.timestamp}{self.transactions}{self.proof}'.encode())
        return sha.hexdigest()

    def recalculate_hash(self):
        self.hash = self.hash_block()

