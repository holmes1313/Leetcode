# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:53:52 2019

@author: z.chen7
"""

# 104. Maximum Depth of Binary Tree
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."""
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    ld = maxDepth(root.left)
    rd = maxDepth(root.right)
    return max(ld, rd) + 1