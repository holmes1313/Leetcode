# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:30:51 2019

@author: z.chen7
"""
# 530. Minimum Absolute Difference in BST
"""
Given a binary search tree with non-negative values, find the minimum 
absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note: There are at least two nodes in this BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if node is None:
                return None

            inorder(node.left)
            if prev[0] is not None:
                min_diff[0] = min(min_diff[0], node.val - prev[0])
            prev[0] = node.val
            inorder(node.right)

        prev = [None]
        min_diff = [float('inf')]
        inorder(root)
        return min_diff[0]