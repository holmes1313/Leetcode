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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return 0
        
        result = [root.val]
        self.helper(root, target, result)
        return result[0]
    
    def helper(self, node, target, result):
        
        if node.val == target:
            result[0] = node.val
            return
        
        if abs(node.val - target) < abs(result[0] - target):
            result[0] = node.val
            
        if node.left:
            self.helper(node.left, target, result)
        if node.right:
            self.helper(node.right, target, result)