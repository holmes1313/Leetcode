# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:08:55 2019

@author: z.chen7
"""
# 112_Path_Sum
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# breath first search
class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """     
        if not root:
            return False
        
        result = []
        queue = collections.deque([(root, root.val)])
        
        while queue:
            
            node, total = queue.pop()
            
            if not node.left and not node.right:
                result.append(total)
                
            if node.left:
                queue.append((node.left, total + node.left.val))
                
            if node.right:
                queue.append((node.right, total + node.left.val))
                
        return result
        

# depth first search
class Solution2(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """    
        if not root:
            return False
        
        results = []
        self.dfs(root, root.val, results)
        return target in results
        
    def dfs(self, node, total, results):
        
        if not node.left and not node.right:
            results.append(total)
            
        if node.left:
            self.dfs(node.left, total + node.left.val, results)
            
        if node.right:
            self.dfs(node.right, total + node.right.val, results)
            
    

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
Solution().hasPathSum(tree1, 2)
