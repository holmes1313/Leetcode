# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:06:47 2019

@author: z.chen7
"""
# 91. Decode Ways
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

# https://leetcode.com/problems/decode-ways/discuss/30358/Java-clean-DP-solution-with-explanation
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(1, len(s)):
            singleDigit = s[i]
            doubleDigits = s[i-1: i+1]
            
            if singleDigit != '0':
                dp[i+1] += dp[i]
                
            if 10 <= int(doubleDigits) <= 26:
                dp[i+1] += dp[i-1]
                
        return dp[len(s)]
                
        