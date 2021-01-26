from time import time
import json
import hashlib
from urllib.parse import urlparse

class Blockchain (object):
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.difficulty = 2
        self.minerRewards = 50
        self.blockSize = 10
        self.nodes = set()


    def getLastBlock(self):
        return self.chain[-1];

    def addBlock(self, block):
        if(len(self.chain)) > 0:
            block.prev = self.getLastBlock().hash;
        else:
            block.prev = 'none';
        self.chain.append(block);

    def chainJSONencode(self):

        blockArrJSON = [];
        for block in self.chain:
            blockJSON = {};
            blockJSON['hash'] = block.hash;
            blockJSON['index'] = block.index;
            blockJSON['prev'] = block.prev;
            blockJSON['time'] = block.time;


            transactionsJSON = [];
            tJSON = {};
            for transaction in block.transactions:
                tJSON['time'] = transaction.time;
                tJSON['sender'] = transaction.sender;
                tJSON['reciever'] = transaction.reciever;
                tJSON['amt'] = transaction.amt;
                tJSON['hash'] = transaction.hash;
                transactionsJSON.append(tJSON);

            blockJSON['transactions'] = transactionsJSON;

            blockArrJSON.append(blockJSON);

        return blockArrJSON;



class Block (object):
    def __init__(self, transactions, time, index):
        self.index = index
        self.transactions = transactions #transaction data
        self.time = time 
        self.prev = '' #hash of previous block
        self.hash = self.calculateHash() # hash of block
        self.nonse = 0

    def calculateHash(self):
        hashTransactions = '';
        for transaction in self. transactions:
            hashTransactions += transaction.hash;
        
        hashString = str(self.time) + hashTransactions + self.prev + str(self.index);
        hashEncoded = json.dumps(hashString, sort_keys=True).encode();
        
        return hashlib.sha256(hashEncoded).hexdigest();


class Transaction (object):
    def __init__(self):
        self.sender = sender;
        self.reciever = reciever;
        self.amt = amt;
        self.time = time();
        self.hash = self.calculateHash();

