# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:00:06 2019

@author: z.chen7
"""

# 101. Symmetric Tree
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            return (node1.val == node2.val) and is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)

        return is_mirror(root.left, root.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [(root.left, root.right)]
        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))

        return True
