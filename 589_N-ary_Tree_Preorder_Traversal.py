# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:21:36 2019

@author: z.chen7
"""

# 589. N-ary Tree Preorder Traversal
"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4]."""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        result.append(root.val)
        for child in root.children:
            result.extend(self.preorder(child))
            
        return result










