"""
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
"""
class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        left_sums= [0] * n
        for i in range(1, n):
            left_sums[i] = left_sums[i-1] + nums[i-1]

        right_sums = [0] * n
        for i in range(n-2, -1 , -1):
            right_sums[i] = right_sums[i+1] + nums[i+1]

        ans = [0] * n
        for i in range(n):
            ans[i] = abs(right_sums[i] - left_sums[i])

        return ans

    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_sum = 0
        total = sum(nums)
        n = len(nums)

        left_sums = []
        right_sums = []

        for i in range(n):
            left_sums.append(left_sum)
            right_sum = total - nums[i] - left_sum
            right_sums.append(right_sum)
            left_sum += nums[i]

        return [abs(left_sums[i] - right_sums[i]) for i in range(n)]
