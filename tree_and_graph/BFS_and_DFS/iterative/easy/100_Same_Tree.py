# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:11:10 2019

@author: z.chen7
"""

# 100. Same Tree

"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is None and q is not None:
            return False

        if q is None and p is not None:
            return False

        if p is not None and q is not None:
            if p.val != q.val:
                return False
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if p is not None and q is not None and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSameTree3(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = []
        stack.append((p, q))

        while stack:
            t1, t2 = stack.pop()

            if t1 is None and t2 is None:
                continue

            if t1 and t2 and t1.val == t2.val:
                stack.append((t1.left, t2.left))
                stack.append( (t1.right, t2.right))
            else:
                return False

        return True

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = deque()
        queue.append((p, q))

        while queue:
            t1, t2 = queue.popleft()
            
            if t1 is None and t2 is None:
                continue

            if t1 and t2 and t1.val == t2.val:
                queue.append((t1.left, t2.left))
                queue.append((t1.right, t2.right))
            else:
                return False

        return True