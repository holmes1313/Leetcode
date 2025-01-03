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
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()
    
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    return True

            if node.right:
                stack.append((node.right, curr_sum + node.right.val))

            if node.left:
                stack.append((node.left, curr_sum + node.left.val))

        return False    

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        targetSum -= root.val

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, targetSum)]
        while stack:
            node, curr_sum = stack.pop()

            if not node.left and not node.right and node.val == curr_sum:
                return True

            if node.left:
                stack.append((node.left, curr_sum - node.val))

            if node.right:
                stack.append((node.right, curr_sum - node.val))


        return False
