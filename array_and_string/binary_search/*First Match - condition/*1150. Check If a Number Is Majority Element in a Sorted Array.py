"""
Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.

A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

 

Example 1:

Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
Example 2:

Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.
"""
class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target not in nums:
            return False

        mid_idx = len(nums) // 2

        first_idx = nums.index(target)
        if first_idx > mid_idx:
            return False
        last_idx = len(nums) - nums[::-1].index(target) - 1
        if last_idx < mid_idx:
            return False
        count = last_idx - first_idx + 1
        return count > len(nums) / 2


    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left += 1
                else:
                    right -= 1
            return left

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left += 1
                else:
                    right -= 1
            return left

        first_idx = find_first(nums, target)
        last_idx = find_last(nums, target) - 1
        count = last_idx - first_idx + 1
        return count > len(nums) / 2

    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        import bisect
        first_idx = bisect.bisect_left(nums, target)
        last_idx = bisect.bisect_right(nums, target) - 1
        return last_idx - first_idx + 1 > len(nums) // 2
