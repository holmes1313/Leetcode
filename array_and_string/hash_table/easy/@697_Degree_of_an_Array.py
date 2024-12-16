#  697. Degree of an Array
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999."""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        first_idx = {}
        last_idx = {}
        max_count = 0
        max_freq_nums = []

        for i, num in enumerate(nums):
            if num not in counts:
                counts[num] = 1
                first_idx[num] = i
                last_idx[num] = i
            else:
                counts[num] += 1
                last_idx[num] = i

            if counts[num] > max_count:
                max_count = counts[num]
                max_freq_nums = [num]
            elif counts[num] == max_count:
                max_freq_nums.append(num)

        min_len = float('inf')
        for num in max_freq_nums:
            min_len = min(min_len, last_idx[num] - first_idx[num]+1)

        return min_len
            