"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""
class Solution:
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def kadane(arr):
            max_sum = float("-inf")
            curr_sum = 0
            for num in arr:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)
            return max_sum

        concat = nums + nums
        n = len(nums)
        max_max = float("-inf")
        for i in range(n):
            curr_max = kadane(concat[i:i+n])
            max_max = max(max_max, curr_max)

        return max_max
        
    def maxSubarraySumCircular(self, nums):
        # Helper function to find the maximum subarray sum using Kadane's algorithm
        def kadane(arr):
            max_sum = float('-inf')
            current_sum = 0
            for num in arr:
                current_sum += num
                max_sum = max(max_sum, current_sum)
                current_sum = max(current_sum, 0)
            return max_sum
        
        total_sum = sum(nums)
        max_subarray_sum = kadane(nums)
        min_subarray_sum = kadane([-num for num in nums])  # Finding the minimum sum subarray
        
        # If total_sum is equal to min_subarray_sum, it means all elements are negative
        if total_sum == -min_subarray_sum:
            return max_subarray_sum
        
        # Return the maximum of the regular max subarray sum or total_sum - min_subarray_sum
        return max(max_subarray_sum, total_sum + min_subarray_sum)
