# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:39:18 2019

@author: z.chen7
"""

# 111. Minimum Depth of Binary Tree

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DPS - Recursion
    def minDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        if root.left:
            return 1 + self.minDepth(root.left)

        if root.right:
            return 1 + self.minDepth(root.right)

        if not root.right and not root.left:
            return 1

    # DPS - Interation
    def minDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 9999
        stack = [(root, 1), ]
        while stack:
            node, temp = stack.pop()
            if not node.left and not node.right:
                ans = min(ans, temp)

            if node.right:
                stack.append((node.right, temp + 1))

            if node.left:
                stack.append((node.left, temp + 1))
        return ans

    # BFS - Interation
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

