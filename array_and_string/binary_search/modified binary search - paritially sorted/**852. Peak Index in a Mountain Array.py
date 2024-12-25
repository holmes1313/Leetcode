"""
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

 
"""
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if mid + 1 < len(arr) and arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return left
