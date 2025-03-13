# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:39:18 2019

@author: z.chen7
"""

# 111. Minimum Depth of Binary Tree

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution(object):
    """
    since we are traversing nodes level-wise, the first node which is a leaf, i.e. both left and right children are null; We will know that this is the node with the minimum depth.
    """
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype
        """
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append((root, 1))
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))


    def minDepth1(self, root):
        """
        :type root: TreeNode
        :rtype
        """
        def get_min_depth(node):
            if not node:
                return 0

            left_depth = get_min_depth(node.left)
            right_depth = get_min_depth(node.right)

            if left_depth == 0 and right_depth == 0:
                return 1

            if left_depth == 0 or right_depth == 0:
                return max(left_depth, right_depth) + 1

            else:
                return min(left_depth, right_depth) + 1

        d = get_min_depth(root)
        return d
