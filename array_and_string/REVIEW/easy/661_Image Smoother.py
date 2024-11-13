"""
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). 
If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).


Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

 

Example 1:


Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
"""
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(img)
        cols = len(img[0])

        smooth_img = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total = 0
                count = 0

                for x in (i-1, i, i+1):
                    for y in (j-1, j, j+1):
                        if 0 <= x < rows and 0 <= y < cols:
                            total += img[x][y]
                            count += 1

                smooth_img[i][j] = total // count

        return smooth_img
        