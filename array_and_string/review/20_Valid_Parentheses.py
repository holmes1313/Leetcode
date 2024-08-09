# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 23:45:03 2019

@author: z.chen7
"""

# 20. Valid Parentheses
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    while ('()' in s) or ('{}' in s) or ('[]' in s):
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
 
    return s == ''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for p in s:
            if p not in right:
                stack.append(p)
            else:
                if not stack or stack.pop() != right[p]:
                    return False
        return not stack


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mappings = {")": "(", "]": "[", "}": "{"}
        for cha in s:
            if cha in mappings:
                if not stack:
                    return False
                top_cha = stack.pop()
                if top_cha != mappings[cha]:
                    return False
            else:
                stack.append(cha)

        return len(stack) == 0 
        