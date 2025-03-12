# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 17:54:41 2019

@author: z.chen7
"""

# 38. Count and Say
"""
Base case: n = 1 print "1"
for n = 2, look at previous string and write number of times a digit is seen and the digit itself. 

In this case, digit 1 is seen 1 time in a row... so print "1 1"

for n = 3, digit 1 is seen two times in a row, so print "2 1"

for n = 4, digit 2 is seen 1 time and then digit 1 is seen 1 so print "1 2 1 1"

for n = 5 you will print "1 1 1 2 2 1"

Consider the numbers as integers for simplicity. e.g. if previous string is "10 1" 
then the next will be "1 10 1 1" and the next one will be "1 1 1 10 2 1"
"""

class Solution(object):
    def __init__(self):
        self.memo = {}
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        if n not in self.memo:
            result = ""
            last = self.countAndSay(n-1)
            index = 0
            while index < len(last):
                char = last[index]
                count = 0
                while index < len(last) and last[index] == char:
                    count += 1
                    index += 1
                result += str(count) + char
                
            self.memo[n] = result
            
        return self.memo[n]

