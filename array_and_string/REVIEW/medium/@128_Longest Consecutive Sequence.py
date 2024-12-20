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
        if not nums:
            return 0

        num_set = set(nums)
        max_streak = 0
        for num in nums:
            if num -1 not in num_set:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                    #num += 1

                max_streak = max(max_streak, curr_streak)

        return max_streak

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()

        curr_streak = 1
        max_streak = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
    
            if nums[i] == nums[i-1] + 1:
                curr_streak += 1
            else:
                
                max_streak = max(max_streak, curr_streak)
                curr_streak = 1

        return max(max_streak, curr_streak)
