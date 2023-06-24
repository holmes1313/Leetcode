# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:03:55 2019

@author: z.chen7
"""
# 110_Balanced_Binary_Tree
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false."""

# recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.memo = {}
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)        
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, node):
        if not node:
            return 0
        if node not in self.memo:
            self.memo[node] = max(self.maxDepth(node.left), self.maxDepth(node.right)) + 1
        return self.memo[node]