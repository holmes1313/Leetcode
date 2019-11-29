# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:17:26 2019

@author: z.chen7
"""

# 298. Binary Tree Longest Consecutive Sequence

"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in 
the tree along the parent-child connections. The longest consecutive path need 
to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def longestConsecutive2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
       
        ans = 0
        queue = collections.deque()
        queue.appendleft((root, 1))
       
        while queue:
            node, length = queue.pop()
            if length > ans:
                ans = length
            for child in [node.left, node.right]:
                if child:
                    if child.val == node.val + 1:
                        queue.appendleft((child, length + 1))
                    else:
                        queue.appendleft((child, 1))
        return ans
   
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
       
        result = [0]
        self.dfs(root, 1, result)
        return result[0]
       
    def dfs(self, node, length, result):
        if length > result[0]:
            result[0] = length
       
        if node.left:
            if node.left.val - node.val == 1:
                self.dfs(node.left, length+1, result)
            else:
                self.dfs(node.left, 1, result)
               
        if node.right:
            if node.right.val - node.val == 1:
                self.dfs(node.right, length+1, result)
            else:
                self.dfs(node.right, 1, result)
               