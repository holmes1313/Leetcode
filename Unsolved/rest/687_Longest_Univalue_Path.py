# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 20:58:46 2019

@author: z.chen7
"""

# 687. Longest Univalue Path

"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. 
This path may or may not pass through the root.
The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2
"""


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype int
        """
        result = [0]
        self.helper(root, result)
        return result[0]
        
    def helper(self, node, result):
        
        if not node:
            return 0
        
        child_left = self.helper(node.left, result)
        child_right = self.helper(node.right, result)
        
        left_len = right_len = 0
        if node.left and node.val == node.left.val:
            left_len = child_left + 1
   
        if node.right and node.val == node.right.val:
            right_len = child_right + 1
            
        result[0] = max(result[0], left_len + right_len)
        return max(left_len, right_len)
        