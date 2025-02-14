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
        n = len(s)
        # dp[i] indicates whether the substring s[0:i] can be segmented into words from the dictionary.
        dp = [False] * (n+1)
        # Base case: empty string can be segmented
        dp[0] = True
        word_set = set(wordDict)
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in word_set:
                    dp[j] = True
        return dp[-1]

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for word in wordDict:
                if i + len(word) <= n and s[i:i+len(word)] == word and dp[i]:
                    dp[i+len(word)] = True 
        return dp[-1]


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        queue = collections.deque([0])
        seen = set([0])
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start, len(s)+1):
                if end in seen:
                    continue
                
                sub_str = s[start: end]
                if sub_str in word_set:
                    seen.add(end)
                    queue.append(end)
        return False

