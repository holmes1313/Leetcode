# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:37:22 2019

@author: z.chen7
"""
# 590. N-ary Tree Postorder Traversal
"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1]."""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        values = []
        
        def postorder(node):
            if not node:
                return

            for child in node.children:
                postorder(child)

            values.append(node.val)

        postorder(root)
        return values

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        values = []
        stack = [root] 
        while stack:
            node = stack.pop()
            if node:
                for child in node.children:
                    stack.append(child)
                values.append(node.val)

        return values[::-1]
                       