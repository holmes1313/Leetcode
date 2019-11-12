# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:46:12 2019

@author: z.chen7
"""
# 702. Search in a Sorted Array of Unknown Size
"""
Given an integer array sorted in ascending order, write a function to search target in nums.  
If target exists, then return its index, otherwise return -1. 
However, the array size is unknown to you. You may only access the array using an 
ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, 
and if you access the array out of bounds, ArrayReader.get will return 2147483647.

 
Example 1:
Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:
You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
"""


"""
The problem is that binary search requires us knowing the length of the list,
so that we can compare it to the target to the midpoint.
It's better to back off exponentially. Try 1, then 2, then 4, then 8 and so on.
This ensures that if the list has length n, we'll find the length in at most
O(log n) time.
Once we find the length, we just perform a (mostly) normal binary search
"""

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        index = 1
        # in the processs, if the element is bigger than target
        # we'll jump over to the binary search part early
        while reader.get(index) < 10000 and reader.get(index) < target:
            index *= 2
        
        # we only need to check between index // 2 and index
        # because the previous iteration ensured reader.get(index // 2) < target
        low = index // 2
        high = index
        while low <= high:
            mid = (low + high) // 2
            middle = reader.get(mid)
            if middle == target:
                return mid
            elif target < middle:
                high = mid - 1
            else:
                low = mid + 1
        return -1
            