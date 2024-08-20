# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 22:43:30 2019

@author: z.chen7
"""

# 1122. Relative Sort Array
"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:
arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
"""

class Solution(object):
    def relativeSortArray2(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        rest = []
        result = []
        counts = collections.Counter(arr1)
        for num in arr2:
            if num in counts:
                result += [num for _ in range(counts[num])]
                del counts[num]
                #counts[num] = 0
        for key in counts.keys():   
            rest += [key for _ in range(counts[key])]

        rest.sort()
        return result + rest

    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count_map = {}
        remaining = []
        result = []

        for num in arr2:
            count_map[num] = 0

        for num in arr1:
            if num in count_map:
                count_map[num] += 1
            else:
                remaining.append(num)

        for num in arr2:
            for _ in range(count_map[num]):
                result.append(num)
        
        remaining.sort()
        result.extend(remaining)
        return result