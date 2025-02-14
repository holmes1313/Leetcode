"""
https://www.1point3acres.com/bbs/thread-644592-1-1.html
"""

class Solution(object):
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