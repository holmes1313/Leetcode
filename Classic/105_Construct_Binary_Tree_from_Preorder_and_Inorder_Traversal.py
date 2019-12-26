# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:26:18 2019

@author: z.chen7
"""

# 105. Construct Binary Tree from Preorder and Inorder Traversal
"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_index = inorder.index(preorder.pop(0))

            root = TreeNode(inorder[root_index])

            root.left = self.buildTree(preorder, inorder[:root_index])
            root.right = self.buildTree(preorder, inorder[root_index+1:])

            return root
