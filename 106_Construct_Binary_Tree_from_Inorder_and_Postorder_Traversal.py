# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 23:23:31 2020

@author: z.chen7
"""

# 106. Construct Binary Tree from Inorder and Postorder Traversal

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_index = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_index])
            
            root.right = self.buildTree(inorder[root_index+1:], postorder)
            root.left = self.buildTree(inorder[:root_index], postorder)
            return root
        
