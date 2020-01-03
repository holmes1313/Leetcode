# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:33:20 2020

@author: z.chen7
"""

# 404. Sum of Left Leaves

"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        result = 0
        queue = collections.deque()
        queue.appendleft((root, False))
        while queue:
            node, is_left = queue.pop()
            if not node.left and not node.right and is_left:
                result += node.val
                
            if node.left:
                queue.append((node.left, True))
            
            if node.right:
                queue.append((node.right, False))
                
        return result