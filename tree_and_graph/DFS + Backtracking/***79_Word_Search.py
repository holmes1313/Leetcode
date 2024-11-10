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
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, index):
            if index == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False

            temp, board[i][j] = board[i][j], "#"

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if dfs(ni, nj, index+1):
                    return True

            board[i][j] = temp
            return False

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False

