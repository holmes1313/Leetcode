# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:05:06 2019

@author: z.chen7
"""

# 289. Game of Life
"""
According to the Wikipedia's article: "The Game of Life, also known simply as 
Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following 
four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. 
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
"""

# 0 -> 1   mark to 2
# 1 -> 0   mark to 3

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        # use a copy board
        copy_board = [row[:] for row in board]
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for dx, dy in neighbors:
                    row_n = row + dx
                    col_n = col + dy

                    if (0 <= row_n < rows) and (0 <= col_n < cols) and copy_board[row_n][col_n] == 1:
                        live_neighbors += 1

                if copy_board[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][col] = 0
                else:
                    if live_neighbors == 3:
                        board[row][col] = 1


    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # in-place modification
        # live 1 -> dead 0: 3
        # dead 0 -> live 1: 2
        rows = len(board)
        cols = len(board[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for dx, dy in neighbors:
                    row_n = row + dx
                    col_n = col + dy

                    if (0 <= row_n < rows) and (0 <= col_n < cols) and board[row_n][col_n] in set([1, 3]):
                        live_neighbors += 1

                if board[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][col] = 3
                if board[row][col] == 0:
                    if live_neighbors == 3:
                        board[row][col] = 2
                    
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 3:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
