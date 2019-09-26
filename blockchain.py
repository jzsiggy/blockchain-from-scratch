from datetime import datetime
from hashlib import sha256

class Blockchain():
    def __init__(self):
        self.blocks =[]
        self.set_genesis_block()
    
    def set_genesis_block(self):
        data = "FirstBlock"
        timestamp = datetime.utcnow()
        prev_hash = 0
        index = 0
        self.hash_block(
            data, timestamp, prev_hash, index
        )

    def is_hash_valid(self, hash):
        return (hash.startswith('000'))

    def hash_block(self, data, timestamp, prev_hash, index):
        hash = ''
        nonce = 0

        while (not self.is_hash_valid(hash)):
            data = "{0}{1}{2}{3}{4}".format(data, timestamp, prev_hash, index, nonce)
            hash = sha256(data.encode()).hexdigest()
            nonce += 1
            # print(hash)
        print("[nonce] ", nonce)
        self.blocks.append(hash)
    
    def get_last_hash(self):
        return (self.blocks[-1])

    def add_new_block(self, data):
        index = len(self.blocks)
        prev_hash = self.get_last_hash()
        timestamp = datetime.utcnow().timestamp()
        self.hash_block(data, timestamp, prev_hash, index)

    def get_blocks(self):
        return (self.blocks)

        
        
        