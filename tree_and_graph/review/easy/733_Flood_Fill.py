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
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        seen = set()
        stack = [(sr, sc)]
        origin = image[sr][sc]
        if origin == color:
            return image

        while stack:
            row, col = stack.pop()
            if 0<= row < len(image) and 0 <= col < len(image[0]):
                if (row, col) not in seen and image[row][col] == origin:
                    image[row][col] = color
                    seen.add((row, col))
                    stack.append((row+1, col))
                    stack.append((row-1, col))
                    stack.append((row, col+1))
                    stack.append((row, col-1))
        return image
                
