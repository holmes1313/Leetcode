# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:30:09 2019

@author: z.chen7
"""

# 204. Count Primes
"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

# Sieve of Eratosthenes

class Solution(object):
    # less than a non-negative number n
    def countPrimes(self, n):        
        if n < 3:
            return 0
        
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        
        for i in range(2, int(n**0.5)+1):
            if primes[i] == 1:
                primes[i*i: n+1: i] = [0] * len(primes[i*i: n+1: i])
                
        return sum(primes)
    
Solution().countPrimes(10)
Solution().countPrimes(11)
Solution().countPrimes(12)



class Solution2(object):
    # up to a non-negative number n
    def countPrimes(self, n):        
        if n < 2:
            return 0
        
        primes = [1] * (n + 1)
        primes[0] = 0
        primes[1] = 0
        
        for i in range(2, int(n**0.5)+1):
            if primes[i] == 1:
                primes[i*i::i] = [0] * len(primes[i*i::i])
                
        return sum(primes)
    
Solution2().countPrimes(10)
Solution2().countPrimes(11)


def listPrimes(n):
    # list all prime numbers before integer n
    if n < 3:
        return 0
    primes = [1] * n
    primes[0] = 0
    primes[1] = 0
    result = []
    for i in range(2, int(n**0.5)+1):
        if primes[i] == 1:
            primes[i*i::i] = [0] * len(primes[i*i::i])
    for i in range(len(primes)):
        if primes[i] == 1:
            result.append(i)
    return result