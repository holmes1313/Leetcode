# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:35:00 2019

@author: z.chen7
"""

# 144. Binary Tree Preorder Traversal
"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.dfs(root, result)
        return result
        
    def dfs(self, node, result):
        if not node:
            return
        
        result.append(node.val)
        self.dfs(node.left, result)
        self.dfs(node.right, result)
        