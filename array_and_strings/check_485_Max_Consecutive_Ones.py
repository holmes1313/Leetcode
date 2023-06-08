"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.



Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        output = 0
        p1 = 0
        while p1 < len(nums):
            temp_ones = 0
            while p1 < len(nums) and nums[p1] == 1:
                temp_ones += 1
                p1 += 1
            output = max(output, temp_ones)
            p1 += 1
        return output

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count)