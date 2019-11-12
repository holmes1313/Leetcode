# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:17:50 2019

@author: z.chen7
"""

# 733. Flood Fill
"""
An image is represented by a 2-D array of integers, each integer representing 
the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of 
the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 
4-directionally to the starting pixel of the same color as the starting pixel, 
plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), 
and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
"""

# breath first search

import collections

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return []

        oldColor = image[sr][sc]
        if oldColor != newColor:
            queue = collections.deque()
            queue.appendleft((sr, sc))
            while queue:
                m, n = queue.pop()
                image[m][n] = newColor
                for x, y in [(m-1, n), (m, n-1), (m, n+1), (m+1, n)]:
                    if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == oldColor:
                        queue.appendleft((x, y))

        return image