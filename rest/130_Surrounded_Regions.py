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
        if not board:
            return
        
        rn = len(board)
        cn = len(board[0])
        
        if rn < 3 or cn < 3:
            return
        
        queue = collections.deque()
        
        for i in range(rn):
            for j in range(cn):
                if (i in [0, rn-1] or j in [0, cn-1]) and board[i][j] == 'O':
                    queue.appendleft((i, j))
                    
        while queue:
            r, c = queue.pop()
            if 0<=r<rn and 0<=c<cn and board[r][c] == 'O':
                board[r][c] = 'D'
                queue.appendleft((r+1, c))
                queue.appendleft((r-1, c))
                queue.appendleft((r, c+1))
                queue.appendleft((r, c-1))
                
        for i in range(rn):
            for j in range(cn):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'