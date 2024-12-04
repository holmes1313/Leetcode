"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 
"""
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Base case: If the list is of length 1 or 0, it's already sorted
        if len(nums) < 2:
            return nums

        # Step 1: Divide the array into two halves
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # Step 2: Recursively sort both halves
        left = self.sortArray(left)
        right = self.sortArray(right)

        return self.merge(left, right)

    def merge(self, left, right):
        sorted_array = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1

        while i < len(left):
            sorted_array.append(left[i])
            i += 1

        while j < len(right):
            sorted_array.append(right[j])
            j += 1

        return sorted_array
