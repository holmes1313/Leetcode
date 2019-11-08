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
        index_hashtable = {}
        max_len = 0
        start = 0
        import pdb;pdb.set_trace()    
        for i, char in enumerate(s):
            if char in index_hashtable:
                max_len = max(max_len, i - start)
                # update start of string index to the next index
                start = max(index_hashtable[char] + 1, start)
                # start = index_hashtable[char] + 1 can't deal with 'abbac'
            index_hashtable[char] = i
        # return should consider the last non-repeated substring
        return max(max_len, len(s) - start)
    
    
def test():
    input = 'baabc'
    output = Solution().lengthOfLongestSubstring(input)
    import pdb;pdb.set_trace()