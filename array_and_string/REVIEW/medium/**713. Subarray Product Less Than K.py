"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 1:
            return 0
        # for each element in the array, we want to explore how many subarrays ending at that element have a product less than k
        product = 1
        start = 0
        count = 0
        for end in range(len(nums)):
            product *= nums[end]

            while product >= k and start <= end:
                product //= nums[start]
                start += 1
            # the number of subarrays ended at end is end - start + 1
            count += end - start + 1

        return count



