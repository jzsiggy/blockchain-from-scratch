from block import Block

class Blockchain():
    def __init__(self):
        self.blocks =[]
        self.set_genesis_block()
    
    def set_genesis_block(self):
        data = "Genesis\t"
        prev_hash = '0'*64
        genesis_block = Block(data, prev_hash)
        self.blocks.append(genesis_block)
    
    def get_last_hash(self):
        last_block = self.blocks[-1]
        last_hash = last_block.hash
        return (last_hash)

    def add_new_block(self, data):
        prev_hash = self.get_last_hash()
        new_block = Block(data, prev_hash)
        self.blocks.append(new_block)

    def get_blocks(self):
        return (self.blocks)

        
        
        