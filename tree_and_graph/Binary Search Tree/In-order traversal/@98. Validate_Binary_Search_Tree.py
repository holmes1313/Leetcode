# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:14:27 2019

@author: z.chen7
"""

# 98. Validate Binary Search Tree
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # recursion
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, low, high = stack.pop()

            if node:
                if node.val <= low or node.val >= high:
                    return False

                stack.append((node.left, low, node.val))
                stack.append((node.right, node.val, high))

        return True

    # in-order traversal
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def inorder(node):
            if not node:
                return True

            if not inorder(node.left):
                return False

            if self.prev is not None and self.prev >= node.val:
                return False
            self.prev = node.val

            return inorder(node.right)

        self.prev = None

        return inorder(root)

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None and self.prev >= node.val:
                self.valid = False
                return
            self.prev = node.val

            inorder(node.right)

        self.prev = None
        self.valid = True
        inorder(root)
        return self.valid