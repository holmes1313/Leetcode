"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = ""
        for cha in s:
            if cha == "(":
                if stack:
                    # it's not outter parethethse
                    ans += cha
                stack.append(cha)
            else:
                stack.pop()
                if stack:
                    # it's not outter parethethse
                    ans += cha            
        return ans

    def removeOuterParentheses1(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        idx_to_remove = set()
        for i, cha in enumerate(s):
            if cha == ")":
                opening_idx = stack.pop()
                if not stack:
                    idx_to_remove.add(opening_idx)
                    idx_to_remove.add(i)
            else:
                stack.append(i)

        ans = []
        for i, cha in enumerate(s):
            if i not in idx_to_remove:
                ans.append(cha)

        return "".join(ans)

