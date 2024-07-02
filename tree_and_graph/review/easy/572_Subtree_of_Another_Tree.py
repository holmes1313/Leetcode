# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:29:37 2019

@author: z.chen7
"""

# 572. Subtree of Another Tree
"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue

            if self.is_same_tree(node, subRoot):   # node == subRoot is wrong
                return True

            stack.append(node.left)
            stack.append(node.right)

        return False
        
    def is_same_tree(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if node1 and node2 and node1.val == node2.val:
            return self.is_same_tree(node1.left, node2.left) and self.is_same_tree(node1.right, node2.right)
        else:
            return False

