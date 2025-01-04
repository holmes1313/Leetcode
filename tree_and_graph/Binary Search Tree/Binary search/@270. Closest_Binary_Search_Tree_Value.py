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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            elif abs(root.val - target) == abs(closest - target):
                closest = min(closest, root.val)

            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest
