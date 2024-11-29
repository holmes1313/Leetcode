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
                

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_mirror(n1, n2):
            if not n1 and not n2:
                return True

            if not n1 or not n2 or n1.val != n2.val:
                return False

            return is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

        if not root:
            return True

        return is_mirror(root.left, root.right)
