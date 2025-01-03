"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:

0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper
 

Example 1:

Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).
Example 2:

Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

"""
class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        
        def find_first(nums, target, low, high):
            left, right = low, high
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        def find_last(nums, target, low, high):
            left, right = low, high
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        count = 0
        n = len(nums)
        for i in range(n):
            # For each nums[i], calculate the valid range for nums[j]: left <= nums[j] <= right
            left = lower - nums[i]
            right = upper - nums[i]
            # Find the first and last valid indices for nums[j] using binary search
            start = find_first(nums, left, i+1, n-1)
            end = find_last(nums, right, i+1, n-1) - 1
            count += end - start + 1

        return count

        