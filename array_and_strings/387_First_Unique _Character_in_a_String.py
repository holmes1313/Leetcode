# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:49:07 2019

@author: z.chen7
"""

# 387. First Unique Character in a String
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

import collections

def firstUniqChar(s):
    """
    :type s:str
    :rtype: int
    """
    # build hash map : character and how often it appears
    # use Counter
    count = collections.Counter(s)
            
    for i, l in enumerate(s):
        if count[l] == 1:
            return i
    
    return -1
                

