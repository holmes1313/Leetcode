# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:10:07 2019

@author: z.chen7
"""

# 560. Subarray Sum Equals K
"""
Given an array of integers and an integer k, 
you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sums = {0: 1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_sums:
                count += prefix_sums[prefix_sum - k]

            if prefix_sum not in prefix_sums:
                prefix_sums[prefix_sum] = 1
            else:
                prefix_sums[prefix_sum] += 1

        return count


class Solution:
    def subarraySum(self, nums, k):
        count = curr_sum = 0
        h = defaultdict(int)
        
        for num in nums:
            # The current prefix sum
            curr_sum += num
            
            # Situation 1:
            # Continuous subarray starts 
            # from the beginning of the array
            if curr_sum == k:
                count += 1
            
            # Situation 2:
            # The number of times the curr_sum − k has occurred already, 
            # determines the number of times a subarray with sum k 
            # has occurred up to the current index
            count += h[curr_sum - k]
            
            # Add the current sum
            h[curr_sum] += 1
                
        return count
    
"""
Sliding Window: Works for fixed-length subarrays or when the array elements follow certain constraints (like being all positive).
Prefix Sum + HashMap: Works for all types of arrays, whether the elements are positive, negative, or zero, and allows us to dynamically track subarray sums as we iterate through the array.
"""

# if all the integers in the array are positive, 
# then sliding window can be used to solve the problem of finding subarrays whose sum equals a given integer k.
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 0:
            return 0
        left = 0  # Left pointer of the sliding window
        current_sum = 0  # Current sum of elements within the window
        result = 0  # Count of subarrays whose sum equals k
        for right in range(len(nums)):
            current_sum += nums[right]  # Add the current element to the window
            
            # While the sum exceeds k, move the left pointer to shrink the window
            while current_sum > k and left <= right:
                current_sum -= nums[left]
                left += 1
            
            # If the sum matches k, increment the result count
            if current_sum == k:
                result += 1
        
        return result