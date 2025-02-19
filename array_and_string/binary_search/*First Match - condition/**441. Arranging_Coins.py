"""
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.


Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1 + 2 + ... + k <= n
        # (1+k)*k // 2 <= n
        # k**2 + k <= 2*n
        # (k + 1/2)**2 <= 2*n + 1/4
        # k <= (2*n + 1/4) ** (1/2) - 1/2
        return int((2 * n + 0.25)**0.5 - 0.5)

    
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(num):
            return (1 + num) * num // 2

        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            # to find the first idx where 1 + 2 + 3 + .. + idx > n
            if helper(mid) <= n:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1
