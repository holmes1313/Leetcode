# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:09:20 2019

@author: z.chen7
"""

# 113. Path Sum II
"""
Given a binary tree and a sum, find all root-to-leaf paths 
where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        current = []
        self.dfs(root, sum, current, result)
        return result
    
    def dfs(self, node, target, current, result):
        
        if not node.left and not node.right and node.val == target:
            current.append(node.val)
            result.append(current[:])
            
        if node.left:
            self.dfs(node.left, target-node.val, current+[node.val], result)
        if node.right:
            self.dfs(node.right, target-node.val, current+[node.val], result)
            
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        current = []
        queue = collections.deque()
        queue.appendleft((root, sum, current))
        
        while queue:
            node, target, curr = queue.pop()
            
            if not node.left and not node.right and node.val == target:
                curr.append(node.val)
                result.append(curr)
                
            if node.left:
                queue.appendleft((node.left, target-node.val, curr+[node.val]))
                
            if node.right:
                queue.appendleft((node.right, target-node.val, curr+[node.val]))
                
        return result