# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:57:09 2019

@author: z.chen7
"""
# 1002. Find Common Characters
# ***
"""
Given an array A of strings made only from lowercase letters, return a list of 
all characters that show up in all strings within the list (including duplicates). 
 For example, if a character occurs 3 times in all strings but not 4 times, 
 you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]"""

import collections
from typing import List

class Solution(object):
    def commonChars2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_counts = collections.Counter(words[0])
        for word in words:
            common_counts &= collections.Counter(word)

        return common_counts.elements()
            
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_counts = collections.Counter(words[0])
        for word in words:
            current_counts = collections.Counter(word)

            for letter in common_counts.keys():
                common_counts[letter] = min(common_counts[letter], current_counts[letter])

        result = []
        for letter, count in common_counts.items():
            for _ in range(count):
                result.append(letter)

        return result