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
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            digit = digits[index]
            letters = phone_map[digit]
            for letter in letters:
                backtrack(index+1, path+letter)

        backtrack(0, "")
        return result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digit_to_chas = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, curr):
            if len(curr) == len(digits):
                result.append("".join(curr))
                return
            
            digit = digits[index]
            chars = digit_to_chas[digit]
            for cha in chars:
                curr.append(cha)
                backtrack(index + 1, curr)
                curr.pop()

        result = []
        backtrack(0, [])
        return result
