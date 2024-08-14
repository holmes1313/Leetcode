# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:02:44 2019

@author: z.chen7
"""

# 66. Plus One
"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321."""

class Solution(object):
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry == 1:
                digit = digits[i]
                digit += 1
                if digit == 10:
                    digit = 0
                    carry = 1
                else:
                    carry = 0

                digits[i] = digit
        if carry == 1:
            digits = [1] + digits

        return digits

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        ones = [0] * n
        ones[-1] = 1

        ans = []
        carry = 0
        for i in range(n - 1, -1, -1):
            carry += ones[i]
            carry += digits[i]

            ans.append(carry % 10)
            carry //= 10

        if carry:
            ans.append(1)

        return ans[::-1]

            
        