# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 22:50:18 2019

@author: z.chen7
"""

# 293. Flip Game

"""
You are playing the following Flip Game with your friend: Given a string that 
contains only these two characters: + and -, you and your friend take turns to 
flip two consecutive "++" into "--". The game ends when a person can no longer 
make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
"""

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        
        result = []
        for i in range(len(s) - 1):
            if s[i:i+2] == '++':
                result.append(s[:i] + '--' + s[i+2:])
                
        return result