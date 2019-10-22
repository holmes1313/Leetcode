# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:47:56 2019

@author: z.chen7
"""
# 1047. Remove All Adjacent Duplicates In String
"""
Given a string S of lowercase letters, a duplicate removal consists of choosing 
two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  
It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, 
and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters."""

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        """
        letters = set(S) 
        while [letter for letter in letters if letter*2 in S]:
            for letter in [letter for letter in letters if letter*2 in S]:
                S = S.replace(letter*2, '')
        return S
        """
        
        result = []
        
        for s in S:
            if result and result[-1] == s:
                result.pop()
                
            else:
                result.append(s)
                
        return ''.join(result)