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

# tree value question
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
        queue = collections.deque([(root, 0)])
        
        while queue:
            node, value = queue.pop()
            if not node.left and not node.right:
                result.append(value + node.val)
            if node.left:
                queue.appendleft((node.left, value + node.val))
            if node.right:
                queue.appendleft((node.right, value + node.val))
                
        return target in result

# depth first search
class Solution2(object):
    def hasPathSum(self, root, target):
        if not root:
            return False
        result = []
        self.helper(root, 0, result)
        return target in result
    
    def helper(self, node, value, result):
        if not node.left and not node.right:
            result.append(value + node.val)
        if node.left:
            self.helper(node.left, value+node.val, result)    
        if node.right:
            self.helper(node.right, value+node.val, result)
            
    

tree1 = TreeNode(1)
tree1.left = TreeNode(2)
Solution().hasPathSum(tree1, 2)
