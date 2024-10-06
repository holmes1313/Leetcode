# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:53:52 2019

@author: z.chen7
"""
# 285. Inorder Successor in BST

"""
Given a binary search tree and a node in it, 
find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Note:
If the given node has no in-order successor in the tree, return null.
It's guaranteed that the values of the tree are unique.
"""

"""
pseudocode

def inorderSucc(node):
    if node has right subtree:
        return leftmost node of right subtree
    else:
        while node is a right child of node.parent:
            node = node.parent
        return node.parent
        
if we hit the very end of the in-order traversal, return None
"""

# https://leetcode.com/problems/inorder-successor-in-bst/discuss/72656/JavaPython-solution-O(h)-time-and-O(1)-space-iterative

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        # right parent is used to save the parent with value > p's value
        right_parent = None
        
        # locate P
        while root.val != p.val:
            if root.val > p.val:
                # only update right parent if right parent > p
                right_parent = root
                root = root.left
            else:
                root = root.right
        #  return the leftmost child of right subtree
        if root.right:
            return self.getLeftMost(root.right)
        else:
            return right_parent
        
    def getLeftMost(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node