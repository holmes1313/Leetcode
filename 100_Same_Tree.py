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
        
        return self.bfs(p) == self.bfs(q)
        
    def bfs(self, node):
        result = []
        queue = collections.deque([node])
        while queue:
            
            node = queue.pop()
            
            if not node:
                result.append(None)
            else:
                result.append(node.val)
                if node.left or node.right:
                    queue.appendleft(node.left)
                    queue.appendleft(node.right)
                
        return result
    
    
class Solution2(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        result_p = []
        result_q = []
        
        self.dfs(p, result_p)
        self.dfs(q, result_q)
        return result_p == result_q 
        
    def dfs(self, node, result):
        if not node:
            result.append(None)
        else:
            result.append(node.val)
            if node.left or node.right:
                self.dfs(node.left, result)
                self.dfs(node.right, result)
        
        
    