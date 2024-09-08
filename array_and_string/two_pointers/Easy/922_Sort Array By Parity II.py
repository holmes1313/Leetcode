"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
"""
class Solution(object):
    def sortArrayByParityII2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [None for _ in range(len(nums))]

        even_idx = 0
        odd_idx = 1

        for num in nums:
            if num % 2 == 0:
                ans[even_idx] = num
                even_idx += 2
            else:
                ans[odd_idx] = num
                odd_idx += 2

        return ans

    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_p = 0
        odd_p = 1
        n = len(nums)
        while even_p < n and odd_p < n:
            while even_p < n and nums[even_p] % 2 == 0:
                even_p += 2

            while odd_p < n and nums[odd_p] % 2 == 1:
                odd_p += 2

            if even_p < n and odd_p < n:
                nums[even_p], nums[odd_p] = nums[odd_p], nums[even_p]

        return nums
