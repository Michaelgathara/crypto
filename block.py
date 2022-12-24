from hashlib import sha256

class Block:
    def __init__(self, index, transcations, temporal, backHash, nonce=0):
        self.index = index
        self.transcations = transcations
        self.temporal = temporal
        self.backHash = backHash
        self.nonce = nonce

    def hashIt(self):
        blockEntry = json.dumps(self.__dict__, sort_keys=True)
        return sha256(blockEntry.encode()).hexdigest()
