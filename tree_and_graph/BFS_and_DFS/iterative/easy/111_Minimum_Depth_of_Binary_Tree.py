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
class Solution(object):
    def minDepth3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append((root, 0))
        min_dept = float('inf')
        
        while queue:
            node, dept = queue.popleft()
            if node is not None:
                if node.left is None and node.right is None:
                    min_dept = min(min_dept, dept+1)

                queue.append((node.left, dept+1))
                queue.append((node.right, dept+1))

        return min_dept

    """
    since we are traversing nodes level-wise, the first node which is a leaf, i.e. both left and right children are null; We will know that this is the node with the minimum depth.
    """
    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype
        """
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append((root, 0))
       
        while queue:
            node, dept = queue.popleft()
            if node is not None:
                if node.left is None and node.right is None:
                    return dept+1

                queue.append((node.left, dept+1))
                queue.append((node.right, dept+1))
        
    def minDepth(self, root):

        if not root:
            return 0

        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        if root.left:
            return 1 + self.minDepth(root.left)

        if root.right:
            return 1 + self.minDepth(root.right)

        if not root.right and not root.left:
            return 1