# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:06:03 2019

@author: z.chen7
"""

# 139. Word Break
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

# dynamic programming
"""
https://www.youtube.com/watch?v=hLQYQ4zj0qg

s = abcd
wordDict = [ab, cd]

dp = [T, F, T, F, T]
dp[1] = False as dp[0] and a not in wordDict
dp[2] = True as dp[0] and ab in wordDict
dp[3] = False as dp[0] and abc not in wordDict
               and dp[2] and c not in wordDict
dp[4] = True as dp[2] and cd in wordDict
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # d[i] is True is substring s[:i] can be segmented in to words found in wordDict
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
    