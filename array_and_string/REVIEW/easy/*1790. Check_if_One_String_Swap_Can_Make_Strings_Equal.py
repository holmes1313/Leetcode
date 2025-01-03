"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
"""

class Solution(object):
    def areAlmostEqual2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diff_count = 0
        if sorted(s1) != sorted(s2):
            return False

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1

        return diff_count <= 2

    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diff_idxes = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_idxes.append(i)
            if len(diff_idxes) > 2:
                return False

        if len(diff_idxes) == 2:
            if s1[diff_idxes[0]] == s2[diff_idxes[1]] and s1[diff_idxes[1]] == s2[diff_idxes[0]]:
                return True
        if not diff_idxes:
            return True
        return False