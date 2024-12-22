# -*- coding: utf-8 -*-
"""
leetcode 

Algorithms

Created on Tue Sep 24 20:32:13 2019

@author: z.chen7
"""

# 9. Palindrome Number

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Handle negative numbers and numbers ending with 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        revered_num = 0
        x_copy = x
        while x_copy > 0:
            revered_num = revered_num * 10 + x_copy % 10
            x_copy //= 10

        return revered_num == x
