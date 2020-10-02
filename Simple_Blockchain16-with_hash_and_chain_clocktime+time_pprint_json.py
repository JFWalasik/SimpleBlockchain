# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:37:00 2020

@author: jfw
"""
#from time 
import time
import hashlib
import json
from pprint import pprint

def quickHash(data):
    """
    creates a sha-256 hash of just the data in a block 
    should this include other stuff?  the previous hash?
    should the timestamp be part of the hash?
    returns a string
    also prints the output
    """
        
    blockString = str(data).encode()
    hashString = hashlib.sha256(blockString).hexdigest()
    #hashString = 
    print(hashString)
    print(' ')
    return hashString


class Block:
    def __init__(self, index, timestamp, data, hash, previousHash):
        self.index = index
        # self.previousIndex = previousIndex 
        # figure out how to get this from the previous block, or use len(Blochchain)
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.previousHash = previousHash
        

class Blockchain:
    def __init__(self,):
        firstBlockData = 'created by jfw' 
        firstBlock = Block(0, time.ctime(), firstBlockData, quickHash(str(firstBlockData)), 'this is the first block: only jfw knows previous hashes')
        # add time.time() to timestamp for 1st block?
        self.chain = [firstBlock]
        
    def addBlock(self, data):
        previousHash = self.chain[-1].hash
        index = self.chain[-1].index + 1
        timestamp = str(time.ctime()) + str(time.time())  
        # time.time() returns time in seconds since 1970, 
        # but gives the same time for each block, unless I make the processor work through a loop...
        # time.ctime() returns clock time        
        hash = quickHash(str(data) + str(previousHash)) # I included the previous hash
        block = Block(index, timestamp, data, hash, previousHash)
        self.chain.append(block)


'''
here's some code to set up some blocks;
below I created a loop to do the same thing

testChain = Blockchain()
testChain.addBlock('made up data one')

testChain.addBlock('made up data2')
# print(' ')
testChain.addBlock('made up data3')

testChain.addBlock('crypto tx')
'''

testChain2 = Blockchain()
numBlocks = 6
testData = 'really important data'
iterations = 1


# while iterations <= numBlocks:
for block in testChain2.chain:
    
    blockData = str(testData) + str(iterations)
    # let's make some time elapse in between block creation,
    # by iterating through a loop for a few seconds
    # otherwise all the timestamps are the same
    # but decrease the amount of time between blocks 
    # by incrementing n by iterations, until iterations = 4
    # or else the time stamp will end up being the same after a half dozen or so blocks
    i = 10000000
    n = 1
    secs = 3
    while n < i:
        if iterations < secs:
            n += iterations
        else:
            n += secs
    testChain2.addBlock(blockData)
    iterations += 1
    if iterations == numBlocks +1:
        break


'''
for block in testChain.chain:
    print(block.__dict__)
    print(' ')
'''

for block in testChain2.chain:
    stringData = block.__dict__
    jsonData = json.dumps(stringData, indent = 3)
    print(jsonData)
    #print(jsonData)
    # pprint sorts the data - 
    # pprint(block.__dict__)
    # json + indent leaves it in the original order
    print(' ')
