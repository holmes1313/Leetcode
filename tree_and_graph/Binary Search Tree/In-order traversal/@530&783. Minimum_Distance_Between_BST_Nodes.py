# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:21:36 2019

@author: z.chen7
"""
# 783. Minimum Distance Between BST Nodes
"""
Given a Binary Search Tree (BST) with the root node root, return the minimum 
difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node):
            if not node:
                return 0

            inorder(node.left)
            
            if pre[0] is not None:
                min_diff[0] = min(min_diff[0], node.val - pre[0])
            pre[0] = node.val
            inorder(node.right)

        min_diff = [float('inf')]
        pre = [None]
        inorder(root)
        return min_diff[0]

