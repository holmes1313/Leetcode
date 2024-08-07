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
# Same type: 563

# For every node, length of longest path which pass it = MaxDepth of its left subtree + MaxDepth of its right subtree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.maxDepth(root)
        
        return self.result
        
    def maxDepth(self, node):
        if not node:
            return 0
        
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        self.result = max(self.result, left + right)
        
        return max(left, right) + 1
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return 0

            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)
            return max(left_path, right_path) + 1

        longest_path(root)
        return diameter


        