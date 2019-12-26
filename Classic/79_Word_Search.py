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
        
    
    
def test():
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]
    word = 'ABCCED'
    output = Solution().exist(board, word)
    assert output == True
   
def test2():
    board = [["a","a"]]
    word = 'aa'
    output = Solution().exist(board, word)
    assert output == True