"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
 
"""
class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        row_mins = [min(row) for row in matrix]
        col_maxs = []
        for i in range(cols):
            c_max = max(matrix[r][i] for r in range(rows))
            col_maxs.append(c_max)

        if max(row_mins) == min(col_maxs):
            return [max(row_mins)]
        else:
            return []


    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        row_mins = [min(row) for row in matrix]
        col_maxs = []
        for i in range(cols):
            c_max = max(matrix[r][i] for r in range(rows))
            col_maxs.append(c_max)

        lucky_nums = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                    lucky_nums.append(matrix[i][j])
        return lucky_nums