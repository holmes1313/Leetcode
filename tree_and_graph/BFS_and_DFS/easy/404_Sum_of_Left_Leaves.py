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
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        stack = [root, ]
        while stack:
            node = stack.pop()

            if node.left and (node.left.left is None) and (node.left.right is None):  # is left leaf
                ans += node.left.val

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return ans

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def helper(node, left_leaves):

            if node.left and (node.left.left is None) and (node.left.right is None):
                left_leaves.append(node.left.val)

            if node.left:
                helper(node.left, left_leaves)

            if node.right:
                helper(node.right, left_leaves)

        left_leaves = []
        helper(root, left_leaves)
        return sum(left_leaves)