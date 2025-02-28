"""
You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.

 

Example 1:

Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.
Example 2:

Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.
 

Constraints:

-1015 <= num <= 1015
"""
class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)

        if num >= 0:
            digits = sorted(num_str)

            if digits[0] == "0":
                for i in range(1, len(digits)):
                    if digits[i] != "0":
                        digits[0], digits[i] = digits[i], digits[0]
                        break

            result = int("".join(digits))
        
        else:
            digits = sorted(num_str[1:], reverse=True)
            result = -int("".join(digits))

        return result

    def smallestNumber(self, num):

        is_negative = num < 0
        num_str = str(abs(num))
        sorted_digits = sorted(num_str, reverse=is_negative)

        if not is_negative:
            if sorted_digits[0] == "0":
                for i in range(1, len(sorted_digits)):
                    if sorted_digits[i] != "0":
                        sorted_digits[0], sorted_digits[i] = sorted_digits[i], sorted_digits[0]
                        break

        result = int("".join(sorted_digits))

        return result if not is_negative else -result