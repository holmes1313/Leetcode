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
        ans = []

        for row in matrix:
            min_val = min(row)
            col_idx = row.index(min_val)

            is_lucky = True
            for row_idx in range(len(matrix)):
                if matrix[row_idx][col_idx] > min_val:
                    is_lucky = False
                    break

            if is_lucky:
                ans.append(min_val)

        return ans

    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lucky_nums = []
        row_mins = []
        col_maxes = {}
        for row in matrix:
            min_val = min(row)
            min_idx = row.index(min_val)
            row_mins.append((min_val, min_idx))

        for min_val, col_idx in row_mins:
            if col_idx not in col_maxes:
                col_maxes[col_idx] = float("-inf")
                for i in range(len(matrix)):
                    col_maxes[col_idx] = max(col_maxes[col_idx], matrix[i][col_idx])
            if min_val == col_maxes[col_idx]:
                lucky_nums.append(min_val)

        return lucky_nums
            