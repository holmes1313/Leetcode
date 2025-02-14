"""
变种亿儿零酒，不是给定的k长度，是所有大于等于k长度的都要删掉，follow up如何优化：时间上已经是O（n)了只能propose空间，问了可不可以只用一个counter来update出现的次数，并没有让implement。
"""

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for cha in s:
            if stack and stack[-1][0] == cha:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([cha, 1])

        chas = [cha * val for cha, val in stack]

        return "".join(chas)

    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(s):
            if stack and s[i] == stack[-1][0]:
                stack[-1][1] += 1
                i += 1
            else:
                if stack and stack[-1][1] >= k:
                    stack.pop()
                    continue
                else:
                    stack.append([s[i], 1])
                    i += 1
        if stack and stack[-1][1] >= k:
            stack.pop()
        return "".join(char * count for char, count in stack)
