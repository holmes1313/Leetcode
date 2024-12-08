"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

"""

class Solution:
    def findMaxAverage2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_ave = sum(nums[:k])
        for i in range(len(nums) - k + 1):
            curr_ave = sum(nums[i:i+k]) / k
            max_ave = max(max_ave, curr_ave)
        return max_ave

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            curr_sum += nums[i]

            if i >= k:
                curr_sum -= nums[i - k]

            if i >= k-1:   
                max_sum = max(max_sum, curr_sum)

        return float(max_sum) / k