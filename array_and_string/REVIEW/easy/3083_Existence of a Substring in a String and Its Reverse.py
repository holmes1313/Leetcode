"""
Given a string s, find any 
substring
 of length 2 which is also present in the reverse of s.

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
    def isSubstringPresent2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reversed_s = s[::-1]
        for i in range(len(s) - 1):
            substring = s[i:i+2]
            if substring in reversed_s:
                return True
        return False

    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sub_count = collections.Counter()
        s_reversed = s[::-1]

        for i in range(len(s) - 1):
            sub_count[s[i:i+2]] += 1

        for i in range(len(s) - 1):
            if s_reversed[i:i+2] in sub_count:
                return True

        return False