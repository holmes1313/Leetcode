# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:58:04 2019

@author: z.chen7
"""

# 771. Jewels and Stones
"""
You're given strings J representing the types of stones that are jewels, 
and S representing the stones you have.  Each character in S is a type of stone you have.  
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct."""

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        output = 0
        counts = collections.Counter(stones)
        for cha in jewels:
            output += counts.get(cha, 0)

        return output


class Solution2(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        ans = 0
        jewels = set(jewels)
        for s in stones:
            if s in jewels:
                ans += 1

        return ans
        