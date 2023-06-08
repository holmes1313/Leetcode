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

from typing import List


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        num = int(''.join([str(d) for d in digits])) + 1
        return list(str(num))
        """
        import collections
        result = collections.deque()
        carry = 1
        while digits or carry:
            num = digits.pop() if digits else 0
            s = num + carry
            
            carry = s // 10
            result.appendleft(s % 10)
            
        return list(result)

    def plusOne2(self, digits: List[int]) -> List[int]:
        # in place method
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                break
        if digits and digits[0] == 0:
            digits = [1] + digits
            # or digits.insert(0, 1)
        return digits
        