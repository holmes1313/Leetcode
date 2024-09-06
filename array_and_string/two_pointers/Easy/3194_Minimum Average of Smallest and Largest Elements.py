"""
You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages.

 

Example 1:

Input: nums = [7,8,3,4,15,13,4,1]

Output: 5.5
"""
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        p1 = 0
        p2 = len(nums) - 1
        min_ave = sum(nums)
        while p1 < p2:
            ave = (nums[p1] + nums[p2]) / 2.0
            min_ave = min(ave, min_ave)
            p1 += 1
            p2 -= 1

        return min_ave