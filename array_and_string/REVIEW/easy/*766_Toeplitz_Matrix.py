"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return True  # An empty matrix is considered Toeplitz

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows - 1):
            for j in range(cols - 1):
                # Check the current element with the one diagonally down-right
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        
        return True