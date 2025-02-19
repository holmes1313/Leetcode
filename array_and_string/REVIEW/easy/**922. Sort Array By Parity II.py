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
        n = len(nums)
        even_idx = 0
        odd_idx = 1
        while odd_idx < n and even_idx < n:
            if nums[even_idx] % 2 == 0:
                even_idx += 2
            elif nums[odd_idx] % 2 == 1:
                odd_idx += 2
            else:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]

        return nums

    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = 1
        n = len(nums)
        while p1 < n and p2 < n:
            if nums[p1] % 2 == 0:
                p1 += 2
                continue

            if nums[p2] % 2 == 1:
                p2 += 2
                continue

            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 2
            p2 += 2

        return nums

    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1 = 0
        p2 = 1
        for i in range(len(nums)):
            if nums[i]  % 2 == 0:
                if i % 2 != 0:
                    nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 2
            else:
                if i % 2 == 0:
                    nums[p2], nums[i] = nums[i], nums[p2]
                p2 += 2

        return nums
 