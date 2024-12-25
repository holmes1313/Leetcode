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
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def kadane(arr):
            max_sum = curr_sum = arr[0]
            for num in arr[1:]:
                curr_sum = max(num, curr_sum + num)  # Either start a new subarray or extend the current one
                max_sum = max(max_sum, curr_sum)  # Track the max sum encountered
            return max_sum
        
        n = len(nums)
        
        # Case 1: Find maximum subarray sum using Kadane's algorithm (non-circular)
        max_kadane = kadane(nums)
        
        # Case 2: Find the maximum subarray sum in the concatenated array nums + nums
        # We concatenate nums with itself to simulate a circular array
        nums_concat = nums + nums
        
        # Find the maximum subarray sum of length at most `n` using Kadane's algorithm
        max_concat = kadane(nums_concat)
        
        # The circular sum is restricted to the subarray within the first `n` elements of the concatenated array
        # We can only use the result from the concatenated array if the subarray length is <= n
        if max_concat > max_kadane:
            return max_concat
        else:
            return max_kadane

    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        concat = nums + nums
        curr_sum = 0
        max_sum = float("-inf")
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, i+len(nums)):
                curr_sum += concat[j]
                max_sum = max(max_sum, curr_sum)
                curr_sum = max(0, curr_sum)

        return max_sum
    