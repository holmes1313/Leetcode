"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lowercase English letters.
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
            if len(stack) >= k - 1 and stack[-(k-1):] == [cha] * (k-1):
                for _ in range(k-1):
                    stack.pop()
            else:
                stack.append(cha)

        return "".join(stack)

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

    def removeDuplicates_at_least_k(self, s, k):
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
