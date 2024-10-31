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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_idx = inorder.index(root.val)

        root.left = self.buildTree(preorder[1: 1+root_idx], inorder[:root_idx])
        root.right = self.buildTree(preorder[1+root_idx:], inorder[root_idx+1:])

        return root