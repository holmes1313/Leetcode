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

# Counter() + - & |


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        
        # the intersection of Counter()
        
        if len(A) <= 1:
            return A
        
        count = collections.Counter(A[0])
        
        for a in A[1:]:
            count &= collections.Counter(a)
        return list(count.elements())


def test():
    A = ["bella","label","roller"]
    result = Solution().commonChars(A)


a = {'a': 4, 'b': 3, 'c': 1}
b = {'a': 1, 'b': 4, 'd': 2}
a = collections.Counter(a)
b = collections.Counter(b)
a + b
a & b
a | b

