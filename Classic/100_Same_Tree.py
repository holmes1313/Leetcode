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

import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = collections.deque()
        queue.appendleft((p, q))
        while queue:
            n1, n2 = queue.pop()
            if n1 and n2 and n1.val == n2.val:
                queue.appendleft((n1.left, n2.left))
                queue.appendleft((n1.right, n2.right))
                
            elif not n1 and not n2:
                continue
                
            else:
                return False
            
        return True
        