"""
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

 

Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
"""
class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for x in range(len(nums)+1):
            count = 0
            for num in nums:
                if num >= x:
                    count += 1
                    if count > x:
                        break
                else:
                    break
            if count == x:
                return x
        return -1

    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        for x in range(n+1):
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1

            if n - left == x:
                return x

        return -1

    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        nums.sort()
        for i in range(0, len(nums)+1):
            # find the first val that >= i
            idx = bisect.bisect_left(nums, i)
            if i == len(nums) - idx:
                return i
        return -1
