# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:59:44 2019

@author: z.chen7
"""

# 278. First Bad Version

"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. """


# binary search

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return None
        
        high = n 
        low = 1
        
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid) == False:
                low = mid + 1
                
            elif (isBadVersion(mid) == True) and (isBadVersion(mid - 1) == False):
                return mid
            
            else:
                high = mid - 1
            
        