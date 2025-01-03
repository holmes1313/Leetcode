"""
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.

"""
class Solution(object):        
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        p1 = 0
        p2 = len(nums) - 1
        max_sum = -1
        while p1 < p2:
            sub_sum = nums[p1] + nums[p2]

            if sub_sum < k:
                max_sum = max(max_sum, sub_sum)
                p1 += 1
            else:
                p2 -= 1

        return max_sum
