"""
Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.

Example 1:
Input: s = "aabb"
Output: ["abba","baab"]

Example 2:
Input: s = "abc"
Output: []
"""
import collections
from typing import List

# time limit exceeded
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        def backtracking(curr, count):
            if len(curr) == len(s) and curr == curr[::-1]:
                result.append("".join(curr[:]))
                return

            for key in count:
                if count[key] > 0:
                    curr.append(key)
                    count[key] -= 1
                    backtracking(curr, count)
                    curr.pop()
                    count[key] += 1

        result = []
        count = collections.Counter(s)
        backtracking([], count)
        return result


class Solution_2:
    def generatePalindromes(self, s: str) -> List[str]:

        def backtracking(curr, count):
            if len(curr) == len(s):
                result.append("".join(curr[:]))
                return

            for key in count:
                if count[key] > 0 and count[key] % 2 == 0:
                    count[key] -= 2
                    backtracking([key] + curr + [key], count)
                    count[key] += 2

        result = []
        count = collections.Counter(s)

        odds = [key for key, val in count.items() if val % 2 != 0]
        if len(odds) > 1:
            return []
        elif len(odds) == 1:
            count[odds[0]] -= 1
            backtracking([odds[0]], count)
        else:
            backtracking([], count)

        return result
