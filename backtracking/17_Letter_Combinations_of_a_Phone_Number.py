# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:30:36 2019

@author: z.chen7
"""

# 17. Letter Combinations of a Phone Number
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        result = []
        current = ""
        index = 0
        self.backtrack(digits, dic, index, current, result)
        return result
    
    def backtrack(self, digits, dic, index, current, result):
        if len(current) == len(digits):
            result.append(current)
        else:
            for c in dic[digits[index]]:
                self.backtrack(digits, dic, index+1, current+c, result)
                # or
                # current += c
                # self.backtrack(digits, dic, index+1, current, result)
                # current = current[:-1]
                

class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        combinations = []
        index = 0
        path = []

        def backtrack(index, path):
            # base case
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                # move on to the next digit
                backtrack(index+1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        backtrack(index, path)
        return combinations