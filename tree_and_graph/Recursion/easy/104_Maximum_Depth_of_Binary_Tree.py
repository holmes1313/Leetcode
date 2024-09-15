# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:53:52 2019

@author: z.chen7
"""

# 104. Maximum Depth of Binary Tree
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, node_dep = stack.pop()
            if node is not None:
                depth = max(depth, node_dep)
                stack.append((node.left, node_dep+1))
                stack.append((node.right, node_dep+1))
        return depth
        

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1