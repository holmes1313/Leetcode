# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:22:31 2019

@author: z.chen7
"""
# 3. Longest Substring Without Repeating Characters
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
import collections


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        cha_count = collections.defaultdict(int)
        for end in range(len(s)):
            cha = s[end]
            cha_count[cha] += 1

            while cha_count[cha] > 1:
                cha_count[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        cha_index = {}
        max_len = 0
        for end in range(len(s)):
            if s[end] in cha_index:
                start = max(cha_index[s[end]] + 1, start)
            cha_index[s[end]] = end
            max_len = max(max_len, end - start + 1)

        return max_len


