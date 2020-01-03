# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:11:32 2019

@author: z.chen7
"""

# 226. Invert Binary Tree

"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = collections.deque()
        queue.appendleft(root)
        while queue:
            node = queue.pop()
            if node:
                node.left, node.right = node.right, node.left
                queue.appendleft(node.left)
                queue.appendleft(node.right)
                
        return root