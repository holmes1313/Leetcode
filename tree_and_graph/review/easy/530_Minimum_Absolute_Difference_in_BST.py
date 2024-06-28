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
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2(object):
    def getMinimumDifference3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = []

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                values.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        values.sort()
        min_diff = values[-1] - values[0]
        for i in range(len(values)-1):
            min_diff = min(min_diff, values[i+1] - values[i])
        return min_diff

    # an inorder traversal handles the nodes in sorted order
    def getMinimumDifference2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nums = []

        def inorder(node):
            if node:
                inorder(node.left)
                nums.append(node.val)
                inorder(node.right)

        inorder(root)
        min_diff = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            min_diff = min(min_diff, nums[i+1] - nums[i])
        return min_diff


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        pre_val = None

        def inorder(node):
            if not node:
                return

            nonlocal min_diff, pre_val
            inorder(node.left)

            if pre_val is not None:
                min_diff = min(min_diff, node.val - pre_val)
            pre_val = node.val
            inorder(node.right)
        
        inorder(root)
        return min_diff