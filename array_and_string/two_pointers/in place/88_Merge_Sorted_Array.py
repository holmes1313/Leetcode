"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]"""

"""
note:
Interview Tip: Whenever you're trying to solve an array problem in-place, always consider the possibility of iterating backwards instead of forwards through the array. 
It can completely change the problem, and make it a lot easier.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # two read pointers and one write pointer 
        # to read values from nums1Copy and nums2 and write them into nums1.
        nums1_copy = nums1[:m]
        curr = p1 = p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1[curr] = nums1_copy[p1]
                p1 += 1
                curr += 1
            else:
                nums1[curr] = nums2[p2]
                p2 += 1
                curr += 1

        while p1 < m:
            nums1[curr] = nums1_copy[p1]
            p1 += 1
            curr += 1

        while p2 < n:
            nums1[curr] = nums2[p2]
            p2 += 1
            curr += 1

        return nums1

    def merge2(self, nums1, m, nums2, n):
        # Whenever you're trying to solve an array problem in place, always consider the possibility of iterating backwards instead of forwards through the array. It can completely change the problem, and make it a lot easier.
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        curr = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[curr] =  nums2[p2]
                curr -= 1
                p2 -= 1
            else:
                nums1[curr] = nums1[p1]
                curr -= 1
                p1 -= 1

        while p2 >= 0:
            nums1[curr] = nums2[p2]
            p2 -= 1
            curr -= 1

        return nums1
