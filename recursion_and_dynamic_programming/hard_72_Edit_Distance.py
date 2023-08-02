"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def recursion(word1, word2, p1, p2):
            if len(word1) == p1 and len(word2) == p2:
                return 0

            if len(word1) == p1:
                return len(word2) - p2

            if len(word2) == p2:
                return len(word1) - p1

            if (p1, p2) not in memo:
                if word1[p1] == word2[p2]:
                    ans = recursion(word1, word2, p1 + 1, p2 + 1)
                else:
                    insert = 1 + recursion(word1, word2, p1, p2 + 1)
                    delete = 1 + recursion(word1, word2, p1 + 1, p2)
                    replace = 1 + recursion(word1, word2, p1 + 1, p2 + 1)
                    ans = min(insert, delete, replace)
                memo[(p1, p2)] = ans
            return memo[(p1, p2)]

        return recursion(word1, word2, 0, 0)


# reference; https://leetcode.com/problems/edit-distance/solutions/159295/python-solutions-and-intuition/