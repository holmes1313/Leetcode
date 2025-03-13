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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        memo = {}
        def height(node):
            if node is None:
                return 0
            
            if node not in memo:
                memo[node] = max(height(node.left), height(node.right)) + 1
            
            return memo[node]

        if not root:
            return True

        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def depth(node):
            if not node:
                return 0
            
            left_depth = depth(node.left)
            if left_depth == -1:
                return -1
            right_depth = depth(node.right)
            if right_depth == -1:
                return -1

            if abs(left_depth - right_depth) > 1:
                return -1

            return max(left_depth, right_depth) + 1

        return depth(root) != -1

    def isBalanced(self, root):
        self.is_balanced = True

        def depth(node):

            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            if abs(left_depth - right_depth) > 1:
                self.is_balanced = False

            return max(left_depth, right_depth) + 1 

        depth(root)
        return self.is_balanced
