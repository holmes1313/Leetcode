"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr = num
                curr_len = 0
                while curr in nums_set:
                    curr_len += 1
                    curr += 1

                longest = max(longest, curr_len)

        return longest

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))
        curr_streak = 1
        max_streak = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                continue
    
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                curr_streak += 1
            else:
                
                max_streak = max(max_streak, curr_streak)
                curr_streak = 1

        return max(max_streak, curr_streak)
