# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:09:51 2020

@author: z.chen7
"""

# 389. Find the Difference

"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
import collections


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter(s)
        for c in t:
            if not counter[c]:
                return c
            counter[c] -= 1

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)

        for cha in c2:
            if c2[cha] > c1.get(cha, 0):
                return cha
            
        return -1