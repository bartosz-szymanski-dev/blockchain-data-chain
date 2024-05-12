from blockchain import Blockchain

if __name__ == "__main__":
    bc = Blockchain()
    bc.add_transaction("Alice", "Bob", 50)
    bc.add_transaction("Bob", "Charlie", 25)
    bc.add_block()

    bc.add_transaction("Alice", "Charlie", 30)
    bc.add_block()

    for block in bc.get_chain():
        print(block)
