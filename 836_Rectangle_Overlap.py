# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:53:29 2019

@author: z.chen7
"""

# 836. Rectangle Overlap
"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the 
coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  
To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
"""

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec2[0] < rec1[2] and rec2[1] < rec1[3] and rec2[2] > rec1[0] and rec2[3] > rec1[1]:
                return True
            
        return False