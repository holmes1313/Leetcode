# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:39:16 2019

@author: z.chen7
"""
# 965. Univalued Binary Tree
"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Example 1:

Input: [1,1,1,1,1,null,1]
Output: true"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [root]
        val = root.val
        while stack:
            node = stack.pop()
            if node:
                if node.val != val:
                    return False
                stack.append(node.left)
                stack.append(node.right)

        return True