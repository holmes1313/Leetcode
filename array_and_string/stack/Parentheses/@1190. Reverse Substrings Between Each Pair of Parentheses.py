"""

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
"""

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for cha in s:
            if cha == ")":
                temp_str = ""
                while stack and stack[-1] != "(":
                    temp_str += stack.pop()
                stack.pop()
                for cha in temp_str:
                    stack.append(cha)
            else:
                stack.append(cha)

        return "".join(stack)

    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for cha in s:
            if cha == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(cha)

        return "".join(stack)
