# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:38:51 2019

@author: z.chen7
"""

# 130. Surrounded Regions
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on 
the border of the board are not flipped to 'X'. Any 'O' that is not on the border 
and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # first identify all 'O's that are connected to the edges of the board and mark them as safe
        # Then, we can capture the remaining 'O's by converting them to 'X's.
        if not board:
            return
        
        rows = len(board)
        cols = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != "O":
                return

            board[i][j] = "S"
            for x, y in directions:
                dfs(i+x, j+y)

        # Mark all 'O's connected to the edges as safe
        for col in range(cols):
            for row in [0, rows-1]:
                if board[row][col] == "O":
                    dfs(row, col)
        for row in range(rows):
            for col in [0, cols-1]:
                if board[row][col] == "O":
                    dfs(row, col)

        # Capture the surrounded regions
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        return board