# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 22:09:05 2019

@author: z.chen7
"""

# 270. Closest Binary Search Tree Value

"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue2(self, root: Optional[TreeNode], target: float) -> int:
        stack = [root]
        ans = root.val
        while stack:
            node = stack.pop()
            if abs(node.val - target) < abs(ans - target):
                ans = node.val
            if (abs(node.val - target) == abs(ans - target)) and (node.val < ans):
                ans = node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def helper(node, target, ans):

            if abs(node.val - target) < abs(ans[0] - target):
                ans[0] = node.val

            if abs(node.val - target) == abs(ans[0] - target)  and node.val < ans[0]:
                ans[0] = node.val

            if node.left:
                helper(node.left, target, ans)

            if node.right:
                helper(node.right, target, ans)

        ans = [root.val]
        helper(root, target, ans)
        return ans[0]