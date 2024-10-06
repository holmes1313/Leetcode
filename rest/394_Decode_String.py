# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:57:24 2019

@author: z.chen7
"""

# 394. Decode String

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits 
and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""

# looks like stack is a better solution
# https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack

# self solution
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        while "[" in s:
            lo = s.rfind('[')
            for i in range(lo+1, len(s)):
                if s[i] == ']':
                    hi = i
                    break
            rep = ''
            rep_idx = lo - 1
            while rep_idx >= 0 and s[rep_idx].isnumeric():
                rep = s[rep_idx] + rep
                rep_idx -= 1
            rep = int(rep)
            
            
            s_list = list(s)
            s_list[rep_idx+1: hi+1] = rep * s_list[lo+1:hi]
            s = ''.join(s_list)
            
        return s
        