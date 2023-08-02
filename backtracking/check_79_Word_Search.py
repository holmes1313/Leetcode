# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 17:29:19 2019

@author: z.chen7
"""

# 79. Word Search
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


# this is a depth first search problem, not breadth first search
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rn = len(board)
        cn = len(board[0])
        
        for i in range(rn):
            for j in range(cn):
                if self.dfs(board, i, j, word, rn, cn):
                    return True
        return False
    
    def dfs(self, board, i, j, word, rn, cn):
        if not word:
            return True
        
        if i < 0 or i >= rn or j < 0 or j >= cn:
            return False
        
        if board[i][j] != word[0]:
            return False
        
        tmp = board[i][j]
        board[i][j] = '_'
        
        """
        # Time Limit Exceeded
        up = self.dfs(board, i-1, j, word[1:], rn, cn)
        down = self.dfs(board, i+1, j, word[1:], rn, cn)
        left = self.dfs(board, i, j-1, word[1:], rn, cn)
        right = self.dfs(board, i, j+1, word[1:], rn, cn)
        result = up or down or left or right
        """
        
        result = (self.dfs(board, i-1, j, word[1:], rn, cn) or
                  self.dfs(board, i+1, j, word[1:], rn, cn) or
                  self.dfs(board, i, j-1, word[1:], rn, cn) or
                  self.dfs(board, i, j+1, word[1:], rn, cn)
                 )
        
        board[i][j] = tmp
        return result


from typing import List


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtracking(row, col, idx):

            if idx == len(word):
                return True

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[row]):
                return False

            if board[row][col] != word[idx]:
                return False

            temp = board[row][col]
            board[row][col] = "_"

            result = (backtracking(row + 1, col, idx + 1) or backtracking(row - 1, col, idx + 1) or backtracking(row,
                                                                                                                 col + 1,
                                                                                                                 idx + 1) or backtracking(
                row, col - 1, idx + 1))

            board[row][col] = temp

            return result

        for r in range(len(board)):
            for c in range(len(board[r])):
                if backtracking(r, c, 0):
                    return True

        return False



