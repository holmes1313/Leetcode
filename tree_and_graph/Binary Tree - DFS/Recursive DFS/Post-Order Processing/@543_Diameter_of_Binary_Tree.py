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

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        diameter = [0]
        diameter_path = []

        def depth(node):
            if not node:
                return 0, []

            left_len, left_path = depth(node.left)
            right_len, right_path = depth(node.right)
            
            # While computing the height, also update the diameter by checking the sum of heights of the left and right subtrees at each node.
            if left_len + right_len > diameter[0]:
                diameter[0] = left_len + right_len 
                diameter_path[:] = left_path + [node.val] + right_path[::-1]

            if left_len > right_len:
                return left_len + 1, left_path + [node.val]
            else:
                return right_len + 1, right_path + [node.val]

        depth(root)
        return diameter[0]
