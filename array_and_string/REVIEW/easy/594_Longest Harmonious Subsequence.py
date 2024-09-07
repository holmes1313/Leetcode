"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0
 
"""
class Solution(object):
    def findLHS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = right = 0
        ans = 0
        while right < len(nums):
            if nums[right] - nums[left] == 0:
                right += 1
            elif nums[right] - nums[left] == 1:
                curr = right - left + 1
                ans = max(ans, curr)
                right += 1
            else:
                while nums[right] - nums[left] > 1:
                    left += 1
        return ans

    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        ans = 0
        for key in counter:
            if key + 1 in counter:
                curr = counter[key] + counter[key+1]
                ans = max(curr, ans)
        return ans

                