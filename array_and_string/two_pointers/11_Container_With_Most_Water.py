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
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0

        while right > left:
            ans = max(ans, (right - left) * min(height[right], height[left]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return ans
                