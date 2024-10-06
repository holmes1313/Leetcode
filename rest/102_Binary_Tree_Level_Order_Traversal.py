# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:13:40 2019

@author: z.chen7
"""

# 102. Binary Tree Level Order Traversal

"""
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        level = 0
        self.dfs(root, level, result)
        return result
    
    def dfs(self, node, level, result):    
        if len(result) < level + 1:
            result.append([])
        result[level].append(node.val)
        
        if node.left:
            self.dfs(node.left, level+1, result)
        if node.right:
            self.dfs(node.right, level+1, result)

 
    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = collections.deque()
        queue.appendleft((root, 0))
        
        while queue:
            node, level = queue.pop()
            
            if len(result) < level + 1:
                result.append([])
                
            result[level].append(node.val)
            
            if node.left:
                queue.appendleft((node.left, level+1))
            if node.right:
                queue.appendleft((node.right, level+1))
                
        return result