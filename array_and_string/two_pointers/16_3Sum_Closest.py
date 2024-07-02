"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        ans = float('inf')
        for idx in range(len(nums)):
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                sum3 = nums[idx] + nums[left] + nums[right]
                if sum3 - target == 0:
                    return sum3
                elif abs(sum3 - target) < abs(ans - target):
                    ans = sum3

                if sum3 < target:
                    left += 1
                else:
                    right -= 1

        return ans
