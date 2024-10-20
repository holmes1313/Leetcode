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
        arr_set = set(arr)
        missing_count = 0
        num = 1
        while num > 0:
            if num not in arr_set:
                missing_count += 1
                if missing_count == k:
                    return num
            num += 1

            
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        missing_count = 0
        curr = 1
        index = 0

        while missing_count < k:
            if index < len(arr) and arr[index] == curr:
                index += 1
                
            else:
                missing_count += 1
                if missing_count == k:
                    return curr
            curr += 1

        return -1
        