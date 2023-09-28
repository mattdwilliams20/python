# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import hashlib

NONCE_LIMIT = 100000000000

Zeroes = 4

def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text= str(block_number) + transactions + previous_hash +str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * Zeroes):
            print(f"Found Hash with Nonce {nonce}")
            return hash_try
    return -1

block_number = 42
transactions = "245uhfiwod43u597"
previous_hash = "37rf8446dhes837l"

mine(block_number,transactions,previous_hash)






