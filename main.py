from blockchain import Blockchain


blockchain = Blockchain()

blockchain.add_new_block("YOO")
blockchain.add_new_block("Third block")
blockchain.add_new_block("Third block")
blockchain.add_new_block("Third block")
blockchain.add_new_block("Third block")
blockchain.add_new_block("Third block")
blockchain.add_new_block("Third block")
blockchain.add_new_block("Third block")


for block in blockchain.get_blocks():
    print(block)