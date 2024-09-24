# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:08:55 2019

@author: z.chen7
"""
# 112_Path_Sum
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        stack = []
        stack.append((root, 0))
        while stack:
            node, curr_sum = stack.pop()
            if node:
                curr_sum += node.val
                if node.left is None and node.right is None:
                    if curr_sum == targetSum:
                        return True

                stack.append((node.left, curr_sum))
                stack.append((node.right, curr_sum))

        return False
    
