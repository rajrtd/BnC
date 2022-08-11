import hashlib as hash

# initialize a block. Note 'transactions' is initialized as an empty list
block = {
    'height': 1,
    'time': 0,
    'prevHash': 'this is the genesis block',
    'merkleRoot': '',
    'transactions': []
}
print("Block: ", block, "\n")

# create a transaction, in this case a string
transaction = 'Pay $1,000,000 to Jeff'
print("Original transaction: ", transaction, "\n")

encoded_tx = transaction.encode()
print("Encoded transaction: ", encoded_tx)

hashed_tx = hash.sha1(encoded_tx)
print("Hashed transaction: ", hashed_tx, "\n")

# Prints out starting with 'b' so you know it's a byte.
print("Hashed transaction (byte object): ", hashed_tx.digest())
print("Hashed transaction (hex object): ", hashed_tx.hexdigest())

hex_tx = hashed_tx.hexdigest()
block["transactions"].append(hex_tx)
print("Transaction is saved to block: ", block, "\n")

# A collision is when a transaction has the same hashed output as another transaction.

# some attributes have been hard-coded for simplicity
block2 = {
    'height':2,
    'time':1,
    'prevHash':'null',
    'merkleRoot': 'null',
    'transactions': []
        }
# create a transaction and add it to the block
tx = hash.sha1('Alice +10'.encode()).hexdigest()
block2["transactions"].append(tx)
block2["merkleRoot"] = tx
print(block2)

hash_block_1 = hash.sha1(block.encode())

