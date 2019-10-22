# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:39:16 2019

@author: z.chen7
"""
# 965. Univalued Binary Tree
"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Example 1:

Input: [1,1,1,1,1,null,1]
Output: true"""

def isUnivalTree(self, root):
    if not root:
        return True
    
    if root.left:
        if root.val != root.left.val:
            return False
        
    if root.right:
        if root.val != root.right.val:
            return False
        
    return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)