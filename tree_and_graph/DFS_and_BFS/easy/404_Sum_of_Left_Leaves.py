# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:33:20 2020

@author: z.chen7
"""

# 404. Sum of Left Leaves

"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isLeaf(self, node):
        return node is not None and node.left is None and node.right is None

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        stack.append(root)
        total = 0

        while stack:
            node = stack.pop()

            if node is not None:

                if self.isLeaf(node.left):
                    total += node.left.val

                stack.append(node.left)
                stack.append(node.right)

        return total
        