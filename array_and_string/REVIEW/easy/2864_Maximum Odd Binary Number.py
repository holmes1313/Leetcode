"""
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

 

Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
Example 2:

Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

"""
class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        # A binary string is odd if and only if the last bit (i.e. the one's place) equals 1
        # to maximize the value of the binary number, we should opt to swap as many 1 bits to the left as we can.
        n = len(s)
        ones_cnt = s.count("1")

        return "1" * (ones_cnt - 1) + "0" * (n - ones_cnt) + "1"
        