# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 22:09:05 2019

@author: z.chen7
"""

# 270. Closest Binary Search Tree Value

"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue2(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_diff = abs(root.val - target)
        ans = root.val 
        stack = [root]

        while stack:
            node = stack.pop()
            if node is not None:
                if node.val == target:
                    return node.val
                else:
                    diff = abs(node.val - target)
                    if diff < min_diff:
                        min_diff = diff
                        ans = node.val
                    elif diff == min_diff:
                        ans = min(node.val, ans)

                if node.val > target:
                    stack.append(node.left)

                if node.val < target:
                    stack.append(node.right)

        return ans

    # Binary Search
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        ans = root.val
        min_diff = abs(root.val - target)

        while root:
            if abs(root.val - target) < min_diff:
                ans = root.val
                min_diff = abs(root.val - target)
            elif abs(root.val - target) == min_diff:
                ans = min(root.val, ans)

            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            else:
                return root.val

        return ans

        