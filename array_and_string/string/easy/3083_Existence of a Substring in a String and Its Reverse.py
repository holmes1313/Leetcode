"""
Given a string s, find any substring of length 2 which is also present in the reverse of s.

Return true if such a substring exists, and false otherwise.

 

Example 1:

Input: s = "leetcode"

Output: true

Explanation: Substring "ee" is of length 2 which is also present in reverse(s) == "edocteel".

Example 2:

Input: s = "abcba"

Output: true

Explanation: All of the substrings of length 2 "ab", "bc", "cb", "ba" are also present in reverse(s) == "abcba".
"""
class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversed_s = s[::-1]
        for i in range(len(s)-1):
            subs = s[i:i+2]
            if subs in reversed_s:
                return True

        return False
