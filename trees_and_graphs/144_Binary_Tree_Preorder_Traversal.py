# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:35:00 2019

@author: z.chen7
"""

# 144. Binary Tree Preorder Traversal
"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, root: Optional[TreeNode], result: List[int]):
        if not root:
            return

        result.append(root.val)
        self.helper(root.left, result)
        self.helper(root.right, result)

    def preorderTraversal_iterate(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        # start with the root node
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                # add right child first then left child
                stack.append(node.right)
                stack.append(node.left)

        return result

