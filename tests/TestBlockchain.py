import unittest
from blockchain import Blockchain
from transaction import Transaction


class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_blockchain_initialization(self):
        self.assertEqual(len(self.blockchain.chain), 1)

    def test_add_transaction(self):
        self.blockchain.add_transaction("Alice", "Bob", 50)
        self.assertEqual(len(self.blockchain.current_transactions), 1)
        self.assertIsInstance(self.blockchain.current_transactions[0], Transaction)

    def test_add_block(self):
        self.blockchain.add_transaction("Alice", "Bob", 50)
        initial_length = len(self.blockchain.chain)
        self.blockchain.add_block()
        self.assertEqual(len(self.blockchain.chain), initial_length + 1)

    def test_chain_validation(self):
        self.blockchain.add_transaction("Alice", "Bob", 50)
        self.blockchain.add_block()
        self.blockchain.add_transaction("Bob", "Charlie", 25)
        self.blockchain.add_block()
        self.assertTrue(self.blockchain.validate_chain())

        if len(self.blockchain.chain) > 1:
            self.blockchain.chain[1].transactions = ["Zmienione dane"]
            self.blockchain.chain[1].recalculate_hash()
        self.assertFalse(self.blockchain.validate_chain())


if __name__ == '__main__':
    unittest.main()
