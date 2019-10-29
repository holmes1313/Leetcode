# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 00:05:39 2019

@author: z.chen7
"""
"""
N marbles are dropped from the opening at the top of the board. 
When a marble hits the peg, it could either go left or right and eventually lands 
in a random bucket. Output should be number of marbles in each bucket at the end (edited) 

For reference
https://images.app.goo.gl/eoYqH3v97bgC5rBMA
"""
from math import factorial

nCk = lambda n, k: factorial(n) / factorial(n - k) / factorial(k)
binom = lambda n, k, p: nCk(n, k) * (p**k) * (1-p)**(n-k)

def get_bucket(num_layer, p, N):
    """
    num_layer: number of layers
    p: prob to go left
    N: number of marbles
    """    
    # number of buckets is equal to num_layer + 1
    # the prob to get into kth bucket, k = 1, 2, 3, ..., num_layer+1
    probs = [binom(num_layer, k, p) for k in range(num_layer+1)]
    
    return [prob * N for prob in probs]
    

layer_num = 10
prob_to_left = 0.5
mable_num = 1000
get_bucket(layer_num, prob_to_left, mable_num)
 