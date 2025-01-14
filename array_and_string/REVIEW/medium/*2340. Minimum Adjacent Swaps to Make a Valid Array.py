"""
You are given a 0-indexed integer array nums.

Swaps of adjacent elements are able to be performed on nums.

A valid array meets the following conditions:

The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.
Return the minimum swaps required to make nums a valid array.

 

Example 1:

Input: nums = [3,4,5,5,3,1]
Output: 6
Explanation: Perform the following swaps:
- Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
- Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
- Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
- Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
- Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
- Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
It can be shown that 6 swaps is the minimum swaps required to make a valid array.
Example 2:
Input: nums = [9]
Output: 0
Explanation: The array is already valid, so we return 0.
"""

class Solution(object):
    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        max_val = max(nums)
        min_idx = nums.index(min_val)
        max_idx = nums[::-1].index(max_val)

        if min_idx <= len(nums) - max_idx - 1:
            swaps = min_idx + max_idx
        else:
            swaps = min_idx + max_idx - 1

        return swaps

    def minimumSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = float("-inf")
        max_last_idx = None
        min_val = float("inf")
        min_first_idx = None

        for i, num in enumerate(nums):
            if num >= max_val:
                max_val = num
                max_last_idx = i
            if num < min_val:
                min_val = num
                min_first_idx = i

        moves = min_first_idx + len(nums) - 1 - max_last_idx
        if min_first_idx > max_last_idx:
            moves -= 1

        return moves
