import hashlib

from block import Block
from transaction import Transaction


class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = [self.create_genesis_block()]

    @staticmethod
    def create_genesis_block():
        return Block(0, '0', [], 100)

    def proof_of_work(self, last_proof, last_hash):
        proof = 0
        while not self.valid_proof(last_proof, proof, last_hash):
            proof += 1

        return proof

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.previous_hash != previous.hash:
                return False

            if not self.valid_proof(previous.proof, current.proof, current.previous_hash):
                return False
        return True

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'

    def add_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        self.current_transactions.append(transaction)

    def add_block(self):
        if self.validate_chain():
            last_block = self.chain[-1]
            new_proof = self.proof_of_work(last_block.proof, last_block.hash)
            new_index = last_block.index + 1
            new_block = Block(new_index, last_block.hash, self.current_transactions, new_proof)
            self.chain.append(new_block)
            self.current_transactions = []
            print(f"Dodano nowy blok #{new_block.index} Hash: {new_block.hash}")
        else:
            raise ValueError("Nieprawidłowy łańcuch, nie można dodać nowego bloku")


    def get_chain(self):
        return [(block.index, block.timestamp, block.transactions, block.hash) for block in self.chain]
