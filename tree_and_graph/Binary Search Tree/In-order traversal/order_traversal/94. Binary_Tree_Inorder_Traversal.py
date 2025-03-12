# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:43:56 2019

@author: z.chen7
"""

# 94. Binary Tree Inorder Traversal
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        ans = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)
        return ans

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Reach the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the node and visit it
            current = stack.pop()
            result.append(current.val)
            
            # Move to the right subtree
            current = current.right
        
        return result