# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:29:50 2019

@author: z.chen7
"""

# 42. Trapping Rain Water
"""
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 
Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
# two pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        leftmax = rightmax = 0
        result = 0
    
        while left < right: 
            if height[left] <= height[right]:  # may trap water on the left side
                if height[left] >= leftmax:  # no high left wall
                    leftmax = height[left]
                else:
                    result += (leftmax - height[left])
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    result += (rightmax - height[right])
                right -= 1

        return result    
                

# understanding what to do
# time limit exceeded
class Solution_2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0    
        result = 0
        for i in range(1, len(height) - 1):
            leftMax = max(height[:i])
            rightMax = max(height[i+1:])
            result += (max(0, min(leftMax, rightMax) - height[i])) 
        return result    