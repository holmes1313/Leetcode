"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtracking(curr, start):

            if len(curr) == k and sum(curr) == n:
                result.append(curr[:])
                return

            if len(curr) > k or sum(curr) > n:
                return

            for i in range(start, 10):
                curr.append(i)
                backtracking(curr, i+1)
                curr.pop()

        result = []
        backtracking([], 1)

        return result
