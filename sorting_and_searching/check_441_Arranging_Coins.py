"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.


Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            curr = (mid + 1) * mid // 2
            if curr <= n < curr + mid + 1:
                return mid
            if curr < n:
                left = mid + 1
            else:
                right = mid - 1
