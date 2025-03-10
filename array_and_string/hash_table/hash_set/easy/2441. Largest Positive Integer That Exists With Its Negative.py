"""
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.

 

Example 1:

Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.
Example 2:

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.
Example 3:

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
"""
class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapping = set()
        ans = 0
        for num in nums:
            if num * (-1) in mapping:
                ans = max(ans, abs(num))

            mapping.add(num)

        return ans if ans > 0 else -1
    

class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums) - 1
        
        while left <= right and nums[right] > 0:
            if -nums[left] == nums[right]:
                return nums[right]

            elif -nums[left] < nums[right]:
                right -= 1
            
            else:
                left += 1

        return -1

        