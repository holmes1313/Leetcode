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

    def isMirror(self, n1, n2):
        if n1 is None and n2 is None:
            return True

        if n1 and n2 and n1.val == n2.val:
            return self.isMirror(n1.left, n2.right) and self.isMirror(n1.right, n2.left)
        else:
            return False

    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.isMirror(root.left, root.right)


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [(root.left, root.right)]

        while stack:
            n1, n2 = stack.pop()

            if n1 is None and n2 is None:
                continue

            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.left, n2.right))
                stack.append((n1.right, n2.left))

            else:
                return False

        return True



        