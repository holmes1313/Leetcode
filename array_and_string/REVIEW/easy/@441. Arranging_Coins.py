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
        # use binary search to find the largest k such that: k*(k+1)//2 <= n
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid+1) // 2

            # if total == n:
            #     return mid
            if total <= n:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1