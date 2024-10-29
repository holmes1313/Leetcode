# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:47:07 2019

@author: z.chen7
"""
# 543. Diameter of Binary Tree
"""
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diameter = [0]
        def depth(node):
            if not node:
                return 0

            left_path = depth(node.left)
            right_path = depth(node.right)
            
            diameter[0] = max(diameter[0], left_path + right_path)
            return max(left_path, right_path) + 1

        depth(root)
        return diameter[0]


        