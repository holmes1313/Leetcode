# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:02:23 2019

@author: z.chen7
"""
# 103. Binary Tree Zigzag Level Order Traversal

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = collections.deque()
        queue.appendleft((root, 0))
        
        while queue:
            node, level = queue.pop()
            
            if len(result) < level + 1:
                result.append([])
            
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].insert(0, node.val)   # adding element to the beginning of a list
                
            if node.left:
                queue.appendleft((node.left, level+1))
            if node.right:
                queue.appendleft((node.right, level+1))
                
        return result
            