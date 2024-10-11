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
        lucky_numbers = []
    
        # Iterate over each row in the matrix
        for row in matrix:
            # Find the minimum value in the row and its index
            min_value = min(row)
            min_index = row.index(min_value)
            
            # Check if the minimum value is the maximum in its column
            is_lucky = True
            for r in range(len(matrix)):
                if matrix[r][min_index] > min_value:
                    is_lucky = False
                    break
            
            if is_lucky:
                lucky_numbers.append(min_value)
        
        return lucky_numbers