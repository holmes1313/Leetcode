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
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right and root.val == target:
            return True
        
        return self.hasPathSum(root.left, target-root.val) or self.hasPathSum(root.right, target-root.val)
        
    
    # DFS would be better than BFS here since it works faster except the worst case.
    # In the worst case the path root->leaf with the given sum is the last considered one and in this case DFS results in the same productivity as BFS.
    def hasPathSum_iterate(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        stack = [(root, target), ]
        while stack:
            node, rest = stack.pop()
            if not node.left and not node.right and node.val == rest:
                return True
            if node.left:
                stack.append((node.left, rest - node.val))
            if node.right:
                stack.append((node.right, rest - node.val))
                
        return False
            
