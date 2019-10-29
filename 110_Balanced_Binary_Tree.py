# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:03:55 2019

@author: z.chen7
"""
# 110_Balanced_Binary_Tree
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false."""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.maxDepth(root) != -1
    
    def maxDepth(self, root):
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1
            




    
tree1  = TreeNode(3)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

tree2 = TreeNode(1)
tree2.right = TreeNode(2)
tree2.right.right = TreeNode(3)
Solution().isBalanced(tree2)


tree3 = TreeNode(1)
tree3.right = TreeNode(2)
tree3.right.right = TreeNode(3)
tree3.right.right.right = TreeNode(4)
tree3.left = TreeNode(2)
tree3.left.left = TreeNode(3)
tree3.left.left.left = TreeNode(4)
Solution().isBalanced(tree3)
