from blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_new_block("First block")
blockchain.add_new_block("Second block")
blockchain.add_new_block("Third block")
blockchain.add_new_block("Fourth block")
blockchain.add_new_block("Fifth block")
blockchain.add_new_block("Sixth block")
blockchain.add_new_block("Seventh block")
blockchain.add_new_block("Eight block")
blockchain.add_new_block("Ninth block")
blockchain.add_new_block("Tenth block")

for block in blockchain.get_blocks():
    print()
    print('\t' + block.to_string())

print()