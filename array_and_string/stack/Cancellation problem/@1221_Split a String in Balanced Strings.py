"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""
class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        for cha in s:
            if stack and stack[-1] != cha:
                stack.pop()
            else:
                stack.append(cha)

            if not stack:
                ans += 1

        return ans
    

import collections


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balanced_subs = 0
        count = collections.defaultdict(int)
        for cha in s:
            count[cha] += 1
            if count["R"] == count["L"]:
                balanced_subs += 1

        return balanced_subs
        