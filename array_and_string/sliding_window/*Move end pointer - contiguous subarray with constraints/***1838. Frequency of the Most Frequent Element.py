"""
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1

"""
class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Sort the array
        nums.sort()
        
        # Initialize the sliding window variables
        start = 0
        max_freq = 1
        current_sum = 0
        
        # Step 2: Iterate through the array with the `end` pointer
        for end in range(len(nums)):
            # Calculate the total cost to make all elements from nums[start] to nums[end] equal to nums[end]
            current_sum += nums[end]
            
            # Check if the window is valid (i.e., the cost to make all elements in the window equal does not exceed k)
            while nums[end] * (end - start + 1) - current_sum > k:
                current_sum -= nums[start]
                start += 1
            
            # Update the max frequency found so far
            max_freq = max(max_freq, end - start + 1)
        
        return max_freq
