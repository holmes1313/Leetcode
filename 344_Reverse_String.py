# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:42:41 2019

@author: z.chen7
"""

# 344. Reverse String
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory."""
s = ["h","e","l","l","o"]
s[::-1]
s

def reserverString(string):
    """ Do not return anything, modify s in-place instead"""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
            
reserverString(s)
print(s)


