# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:43:56 2019

@author: z.chen7
"""

# 94. Binary Tree Inorder Traversal
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    # define a helper function to implement recursion.
    def helper(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return

        self.helper(node.left, result)
        result.append(node.val)
        self.helper(node.right, result)
