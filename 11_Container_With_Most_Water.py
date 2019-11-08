# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:32:28 2019

@author: z.chen7
"""

# 11. Container With Most Water
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point 
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis 
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


# Start by evaluating the widest container, using the first and the last line. 
# All other possible containers are less wide, so to hold more water, they need to be higher.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        
        area = self.calculateArea(left, right, height)
        
        while left < right:
            if height[left] > height[right]:
                right -= 1
                area = max(area, self.calculateArea(left, right, height))
            
            else:
                left += 1
                area = max(area, self.calculateArea(left, right, height))
                
        return area
                
    def calculateArea(self, left, right, height):
        return (right - left) * min(height[left], height[right]) 
                