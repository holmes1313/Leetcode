"""
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

 

Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
Example 2:

Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.
Example 3:

Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.
 

Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
"""

class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        max_ones = 0
        curr_ones = 0
        max_zeros = 0
        curr_zeros = 0

        for cha in s:
            if cha == "1":
                curr_ones += 1
            else:
                max_ones = max(max_ones, curr_ones)
                curr_ones = 0

            if cha == "0":
                curr_zeros += 1
            else:
                max_zeros = max(max_zeros, curr_zeros)
                curr_zeros = 0
        max_ones = max(max_ones, curr_ones)
        max_zeros = max(max_zeros, curr_zeros)
            
        return max_ones > max_zeros

    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        curr_count = 1
        max_ones = 0
        max_zeros = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr_count += 1
            else:
                if s[i] == "1":
                    max_zeros = max(max_zeros, curr_count)
                else:
                    max_ones = max(max_ones, curr_count)
                curr_count = 1

        if s[-1] == "1":
            max_ones = max(max_ones, curr_count)
        else:
            max_zeros = max(max_zeros, curr_count)

        return max_ones > max_zeros
