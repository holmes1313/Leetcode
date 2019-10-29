# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:29:37 2019

@author: z.chen7
"""

# 572. Subtree of Another Tree
"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# similar to 100. Same Tree
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_result = []
        t_result = []
        self.dfs(s, s_result)
        self.dfs(t, t_result)
        # print ''.join(t_result) 
        # print ''.join(s_result)
        return ''.join(t_result) in ''.join(s_result)
        
    
    def dfs(self, node, result):
        
        if not node:
            result.append('$')
        else:
            result.append('^' + str(node.val))
            self.dfs(node.left, result)
            self.dfs(node.right, result)
        