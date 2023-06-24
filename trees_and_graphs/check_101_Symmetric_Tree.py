# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:00:06 2019

@author: z.chen7
"""

# 101. Symmetric Tree
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.helper(p.left, q.right) and self.helper(p.right, q.left)
        else:
            return False

    def isSymmetric_iteration(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right), ]
        while stack:
            q, p = stack.pop()

            if not p and not q:
                continue

            if p and q and p.val == q.val:
                stack.append((q.left, p.right))
                stack.append((q.right, p.left))
            else:
                return False

        return True

