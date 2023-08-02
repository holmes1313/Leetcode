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
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []

        def backtracking(curr, index):
            if len(curr) == len(digits):
                result.append("".join(curr))
                return

            letters = mapping[digits[index]]
            for l in letters:
                curr.append(l)
                backtracking(curr, index+1)
                curr.pop()

        backtracking([], 0)
        return result