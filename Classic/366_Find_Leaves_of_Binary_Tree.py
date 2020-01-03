# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 23:06:19 2020

@author: z.chen7
"""

# 366. Find Leaves of Binary Tree

"""
Given a binary tree, collect a tree's nodes as if you were doing this: 
    Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # use depth to group node values
        result = []
        self.maxDepth(root, result)
        return result
        
        
    def maxDepth(self, node, result):
        if not node:
            return 0
        
        left = self.maxDepth(node.left, result)
        right = self.maxDepth(node.right, result)
        depth = max(left, right) + 1
        
        if len(result) < depth:
            result.append([])
        result[depth - 1].append(node.val)
        return depth
            
        
        
        
        
        