# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:21:36 2019

@author: z.chen7
"""
# 783. Minimum Distance Between BST Nodes
"""
Given a Binary Search Tree (BST) with the root node root, return the minimum 
difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2(object):
    def minDiffInBST2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = []

        def inorder(node):
            if not node:
                return None

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        min_diff = values[-1] - values[0]
        for i in range(len(values) - 1):
            min_diff = min(min_diff, values[i+1] - values[i])
        return min_diff

from typing import Optional

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev_val = None
        min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            
            nonlocal prev_val, min_diff
            inorder(node.left)

            if prev_val is not None:
                min_diff = min(min_diff, node.val - prev_val)
            prev_val = node.val

            inorder(node.right)

        inorder(root)
        return min_diff