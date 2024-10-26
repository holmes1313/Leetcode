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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        stack = [(root, root.val, [root.val])]
        result = []

        while stack:
            node, curr_sum, path = stack.pop()

            if not node.left and not node.right:
                if curr_sum == targetSum:
                    result.append(path)

            if node.left:
                stack.append((node.left, curr_sum+node.left.val, path+[node.left.val]))

            if node.right:
                stack.append((node.right, curr_sum+node.right.val, path+[node.right.val]))

        return result
        