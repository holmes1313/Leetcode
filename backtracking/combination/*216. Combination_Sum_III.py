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
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, 10))

        def backtrack(start, path, curr_sum):
            if len(path) == k:
                if curr_sum == n:
                    result.append(path[:])
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path, curr_sum + nums[i])
                path.pop()

        result = []
        backtrack(0, [], 0)
        return result

        