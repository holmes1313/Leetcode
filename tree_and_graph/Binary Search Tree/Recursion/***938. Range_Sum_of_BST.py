# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:08:38 2019

@author: z.chen7
"""

# 938. Range Sum of BST
"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.


Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root is None:
            return 0

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0

        range_sum = 0

        if low <= root.val <= high:
            range_sum += root.val

        # If the current node's value is greater than low, we should explore the left subtree
        if root.val > low:
            range_sum += self.rangeSumBST(root.left, low, high)

        # If the current node's value is less than high, we should explore the right subtree
        if root.val < high:
            range_sum += self.rangeSumBST(root.right, low, high)

        return range_sum
