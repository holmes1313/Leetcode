# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:30:51 2019

@author: z.chen7
"""
# 530. Minimum Absolute Difference in BST
"""
Given a binary search tree with non-negative values, find the minimum 
absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note: There are at least two nodes in this BST.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# In-order traversal
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        diffs = []
        self.dfs(root, diffs)
        min_diff = diffs[-1] - diffs[0]
        for i in range(1, len(diffs)):
            min_diff = min(min_diff, diffs[i] - diffs[i-1])
        return min_diff    
        
    def dfs(self, node, result):
        if node.left:
            self.dfs(node.left, result)
            
        result.append(node.val)
        
        if node.right:
            self.dfs(node.right, result)
        