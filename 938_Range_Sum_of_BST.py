# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:08:38 2019

@author: z.chen7
"""

# 938. Range Sum of BST
"""
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.


Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
   
def rangeSumBST(root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """    
    # in-order traversal
    if not root:
        return 0
    
    s = 0
    
    if root.val > R:
        s += rangeSumBST(root.left, L, R)
        
    if root.val < L:
        s += rangeSumBST(root.right, L, R)
        
    if L <= root.val <= R:
        s += root.val + rangeSumBST(root.right, L, R) + rangeSumBST(root.left, L, R)
        
    return s

tree = TreeNode(15)
tree.left = TreeNode(7)
tree.right = TreeNode(20)

rangeSumBST(tree, 7, 15)
