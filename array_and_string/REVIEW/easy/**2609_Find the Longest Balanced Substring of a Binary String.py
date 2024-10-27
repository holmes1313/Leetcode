"""
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.
Example 2:

Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4. 
Example 3:

Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0.
"""

class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i in range(len(s) - 1):
            if s[i] == "0" and s[i+1] == "1":
                p1 = i
                p2 = i+1
                count = 0
                while p1 >= 0 and p2 < len(s): 
                    if s[p1] == "0" and s[p2] == "1":
                        count += 1
                        p1 -= 1
                        p2 += 1
                    else:
                        break
                ans = max(ans, count)

        return ans * 2
                



        