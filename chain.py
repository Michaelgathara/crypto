import time
from block import Block

class Chain:
    def __init__(self):
        self.queuedTransactions = []
        self.chain = []
        self.genGenesisBlock()
    
    def genGenesisBlock(self):
        genesisBlock: Block = Block(0, [], time.time(), "0")
        genesisBlock.hash = genesisBlock.hashIt()
        self.chain.append(genesisBlock)
    
    @property
    def previousBlock(self):
        return self.chain[-1]

    diff = 1
    def workProof(self, block):
        block.nonce = 0
        comHash = block.hashIt()
        while not comHash.startswith('0', Chain.diff):
            block.nonce += 1
            comHash = block.hashIt()
        return comHash
    
    def addBlock(self, block, proof) -> bool:
        prevHash = self.prevBlock.hash
        if prevHash != block.prevHash:
            return False
        if not self.validProof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
    
    def validProof(self, block, blockHash) -> bool:
        return blockHash.startswith('0', Chain.diff) and blockHash == block.hashIt()
    
    def newTransaction(self, transaction):
        self.queuedTransactions.append(transaction)
    
    def mine(self):
        if not self.queuedTransactions:
            return False
        
        previousBlock = self.previousBlock

        newBlock = Block(previousBlock.index + 1, self.queuedTransactions, time.time(), previousBlock.hash)

        proof = self.validProof(newBlock)
        self.addBlock(newBlock, proof)
        self.queuedTransactions = []
        return newBlock.index
         