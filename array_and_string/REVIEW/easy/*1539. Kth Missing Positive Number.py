"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

"""
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        missing_count = 0
        idx = 0
        curr = 1
        while True:
            if idx < len(arr) and arr[idx] == curr:
                idx += 1
            else:
                missing_count += 1
                if missing_count == k:
                    return curr
            curr += 1
 
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr_set = set(arr)
        i = 1
        count = 0
        while True:
            if i not in arr_set:
                count += 1
                if count == k:
                    return i
            i += 1
            