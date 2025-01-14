"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
"""
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s1 = []
        for i, cha in enumerate(s):
            if cha == ")":
                if stack:
                    stack.pop()
                    s1.append((cha, i))
            elif cha == "(":
                stack.append(i)
                s1.append((cha, i))
            else:
                s1.append((cha, i))

        ans = []        
        for cha, i in s1:
            if cha == "(" and i in stack:
                continue
            else:
                ans.append(cha)
        return "".join(ans)


    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        index_to_remove = set()

        for i, cha in enumerate(s):
            if cha == "(":
                stack.append(i)
            elif cha == ")":
                if stack:
                    stack.pop()
                else:
                    index_to_remove.add(i)

        for idx in stack:
            index_to_remove.add(idx)

        ans = []
        for i in range(len(s)):
            if i in index_to_remove:
                continue
            else:
                ans.append(s[i])

        return "".join(ans)

