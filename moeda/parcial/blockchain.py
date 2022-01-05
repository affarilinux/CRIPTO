import datetime
import hashlib
import json


class Blockchain:

    def __init__(self):

        self.chain = [] # lista
        self.create_block(proof = 1, previous_hash = '0')

    def create_block (self, proof, previous_hash):
       
        #dicionario
        block = {'index':        len(self.chain) +1, # indice do bloco
                'timestemp' :    str(datetime.datetime.now()), # data em texto
                'proof':         proof,
                'previous_hash': previous_hash
        
        }

        self.chain.append(block) # block adicionar dentro da lista
        return block

    def get_previous_block(self):

        return self.chain[-1] # returno bloco anterior

    def proof_of_work(self, previous_proof):

        new_proof = 1
        check_proof = False

        while check_proof is False: # estive como false

            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:4] == "0000":

                check_proof =  True
            
            else:
                new_proof += 1

        return new_proof 

    def hash(self, block):

        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()# formato hexadecimal

    def is_chain_valid( self, chain):

        previous_block = chain[0]
        block_index    = 1

        while block_index < len(chain):

            block = chain[block_index]

            if block ['previous_hash'] != self.hash(previous_block):
                return False

            previous_proof = previous_block['proof']

            proof = block [ 'proof']

            hash_operation = hashlib.sha256
            


