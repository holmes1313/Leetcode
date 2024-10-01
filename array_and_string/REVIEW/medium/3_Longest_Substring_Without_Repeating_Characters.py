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

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        for left in range(len(s)):
            cha_set = set()
            curr_len = 0
            right = left
            while right < len(s):
                if s[right] not in cha_set:
                    cha_set.add(s[right])
                    curr_len += 1
                    right += 1
                else:
                    break
            max_len = max(max_len, curr_len)

        return max_len

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = 0
        index_map = {}
        max_len = 0
        while right < len(s):
            cha = s[right]
            if cha not in index_map:
                index_map[cha] = right
            else:
                left = max(index_map[cha] + 1, left)
                index_map[cha] = right
            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len
                

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
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
                


