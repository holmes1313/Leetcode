"""
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
"""
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        diff_indx = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indx.append(i)
                if len(diff_indx) > 2:
                    return False

        if len(diff_indx) == 2:
            return s[diff_indx[0]] == goal[diff_indx[1]] and s[diff_indx[1]] == goal[diff_indx[0]]

        if len(diff_indx) == 0:
            return len(set(s)) < len(s)

        return False