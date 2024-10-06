# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:13:34 2019

@author: z.chen7
"""
# 538. Convert BST to Greater Tree

"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every 
key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, [0])
        return root
        
    def helper(self, node, current):
        if not node:
            return
        
        self.helper(node.right, current)
        node.val += current[0]
        current[0] = node.val
        self.helper(node.left, current)
        
        