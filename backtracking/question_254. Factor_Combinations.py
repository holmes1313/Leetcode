"""
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].



Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
"""
import math
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        def backtracking(curr, target, start):
            if curr:
                result.append(curr + [target])

            for i in range(start, int(math.sqrt(target)) + 1):
                if target % i == 0:
                    curr.append(i)
                    backtracking(curr, target // i, i)
                    curr.pop()

        result = []
        backtracking([], n, 2)
        return result


class Solution_slow:
    def getFactors(self, n: int) -> List[List[int]]:

        def backtracking(curr, target, start):
            if curr and target >= curr[-1]:
                result.append(curr + [target])

            for i in range(start, target):
                if target % i == 0:
                    curr.append(i)
                    backtracking(curr, target // i, i)
                    curr.pop()

        result = []
        backtracking([], n, 2)
        return result