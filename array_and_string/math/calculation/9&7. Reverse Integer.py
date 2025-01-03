"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x
        
        x_reversed = 0

        while x > 0:
            x_reversed = x_reversed * 10 + x % 10
            x //= 10
        
        if x_reversed > 2**31 - 1:
            return 0

        if is_negative:
            x_reversed = -x_reversed

        return x_reversed
