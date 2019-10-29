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
                 if self.dfs(board, word, i, j):
                     return True
        return False        
   
    
    # check whether can find word, start at (i,j) position 
    def dfs(self, board, word, i, j):
        if len(word) == 0:  # all the characters are checked
                return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] != word[0]:
            return False
        else:
            holder, board[i][j] = board[i][j], '_'   # marked as visited for situation like board = [['a', 'a']], word = 'aaa'
    
            up = self.dfs(board, word[1:], i-1, j)
            down = self.dfs(board, word[1:], i+1, j)
            left = self.dfs(board, word[1:], i, j-1)
            right = self.dfs(board, word[1:], i, j+1)
            
            board[i][j] = holder
            
            return up or down or left or right

    
    
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