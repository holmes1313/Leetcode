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
class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        left = right = 0
        ans = 0
        index_map = {}
        while right < len(s):
            if s[right] in index_map:
                # start = index_hashtable[char] + 1 can't deal with 'abbac'
                left = max(index_map[s[right]] + 1, left)
            index_map[s[right]] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans

    def lengthOfLongestSubstring2(self, s: str) -> int:
        ans = 0
        start = 0
        max_index = {}
        for i, char in enumerate(s):
            if char in max_index:
                # start = index_hashtable[char] + 1 can't deal with 'abbac'
                start = max(start, max_index[char] + 1)

            ans = max(ans, i - start + 1)
            max_index[char] = i

        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        ans = 0
        count_map = collections.defaultdict(int)
        while right < len(s):
            count_map[s[right]] += 1
            while count_map[s[right]] == 2:
                count_map[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
