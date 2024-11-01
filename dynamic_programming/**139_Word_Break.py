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
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)      # dp[i] indicates whether the substring s[0:i] can be segmented into words from the dictionary.
        dp[0] = True   # Base case: empty string can be segmented
        
        for i in range(1, n+1):
            # For each position in the string, check possible previous positions to see if a valid word can form the substring.
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    # If dp[j] is True and the substring from j to i is in the word dictionary, then set dp[i] to True.
                    dp[i] = True
                    break  # Early exit for this i

        return dp[n]