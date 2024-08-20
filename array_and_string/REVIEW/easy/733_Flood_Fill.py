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

    def neighbors(self, image, row, col, initial_col):
        row_max = len(image)
        col_max = len(image[0])
        neighbors = []
        if row + 1 < row_max:
            neighbors.append((row+1, col))
        if row - 1 >= 0:
            neighbors.append((row-1, col))
        if col + 1 < col_max:
            neighbors.append((row, col+1))
        if col - 1 >= 0:
            neighbors.append((row, col-1))

        return neighbors

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        queue.append((sr, sc))
        initial_col = image[sr][sc]
        explored = {(sr, sc)}

        while queue:
            row, col = queue.popleft()
            image[row][col] = color

            for loc in self.neighbors(image, row, col, initial_col):
                if loc not in explored and image[loc[0]][loc[1]] == initial_col:
                    explored.add(loc)
                    queue.append(loc)

        return image
    

class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        stack = []
        stack.append((sr, sc))
        ori_col = image[sr][sc]

        while stack:
            row, col = stack.pop()
            if row >= len(image) or col >= len(image[0]) or row < 0 or col < 0 or (row, col) in seen:
                continue

            if image[row][col] == ori_col:
                image[row][col] = color
                stack.append((row+1, col))
                stack.append((row-1, col))
                stack.append((row, col+1))
                stack.append((row, col-1))
                seen.add((row, col))

        return image


        