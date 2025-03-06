"""
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 

Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.

"""
class Solution(object):
    def minSwaps(self, nums):
        k = sum(nums)
        n = len(nums)

        if k == n or k == 0:
            return 0

        ones = 0
        max_ones = 0
        for i in range(n+k):
            if nums[i % n] == 1:
                ones += 1

            if i >= k:
                if nums[i-k] == 1:
                    ones -= 1

            max_ones = max(max_ones, ones)

        return k - max_ones

    def minSwaps(self, nums):
        k = sum(nums)
        n = len(nums)

        if k == n or k == 0:
            return 0

        curr_ones_in_window = sum(nums[:k])
        max_ones_in_window = curr_ones_in_window
        for i in range(k, n+k):
            curr_ones_in_window += nums[i % n] - nums[(i-k) % n]
            max_ones_in_window = max(max_ones_in_window, curr_ones_in_window)
        return k - max_ones_in_window