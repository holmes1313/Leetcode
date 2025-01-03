"""
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.



 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.


"""

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        for cha in s:
            if cha == "(":
                stack.append(cha)
                ans = max(ans, len(stack))
            elif cha == ")":
                stack.pop()

        return ans
        