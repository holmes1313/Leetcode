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
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_backtracking:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtracking(curr, node):
            if node is None:
                return

            curr.append(node.val)
            if node.left is None and node.right is None and sum(curr) == targetSum:
                result.append(curr[:])
                curr.pop()  # pop the node once we are done processing ALL of it's subtrees.
                return

            backtracking(curr, node.left)
            backtracking(curr, node.right)
            curr.pop()

        result = []
        backtracking([], root)
        return result


class Solution_DPS(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        def helper(node, curr, target):
            if node.val == target and node.left is None and node.right is None:
                curr.append(node.val)
                result.append(curr[:])

            if node.left:
                helper(node.left, curr + [node.val], target - node.val)

            if node.right:
                helper(node.right, curr + [node.val], target - node.val)

        result = []
        helper(root, [], targetSum)
        return result

    def pathSum2(self, root, targetSum):

        if not root:
            return []
        result = []
        stack = [(root, [], targetSum)]
        while stack:
            node, curr, target = stack.pop()
            if node.val == target and node.left is None and node.right is None:
                curr.append(node.val)
                result.append(curr[:])

            if node.left:
                stack.append((node.left, curr + [node.val], target - node.val))

            if node.right:
                stack.append((node.right, curr + [node.val], target - node.val))

        return result