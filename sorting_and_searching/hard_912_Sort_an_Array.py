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
from typing import List


# merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr, left, right):
            if left == right:
                return arr
            mid = (left + right) // 2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid+1, right)
            merge(arr, left, mid, right)

            return arr

        def merge(arr, left, mid, right):
            l_half = arr[left: mid+1]
            r_half = arr[mid+1: right+1]
            i = 0     # Initial index of first subarray
            j = 0     # Initial index of second subarray
            k = left # Initial index of merged subarray
            while i < len(l_half) and j < len(r_half):
                if l_half[i] < r_half[j]:
                    arr[k] = l_half[i]
                    i += 1
                else:
                    arr[k] = r_half[j]
                    j += 1
                k += 1
            while i < len(l_half):
                arr[k] = l_half[i]
                i += 1
                k += 1
            while j < len(r_half):
                arr[k] = r_half[j]
                j += 1
                k += 1

        return mergeSort(nums, 0, len(nums)-1)
