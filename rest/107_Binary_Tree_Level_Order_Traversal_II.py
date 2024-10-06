# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:49:15 2019

@author: z.chen7
"""
# 107_Binary_Tree_Level_Order_Traversal_II
"""
Given a binary tree, return the bottom-up level order traversal of its nodes' 
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# tree level question

import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        hashtable = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        while queue:
            node, level = queue.pop()
            hashtable[level].append(node.val)
            if node.left:
                queue.appendleft((node.left, level+1))
            if node.right:
                queue.appendleft((node.right, level+1))

        return [hashtable[i] for i in range(len(hashtable)-1, -1, -1)]
    
    
    
class Solution_2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        hashtable = collections.defaultdict(list)
        level = 0
        self.dfs(root, level, hashtable)
        return [hashtable[i] for i in range(len(hashtable) - 1, -1, -1)]
    
    def dfs(self, node, level, hashtable):
        hashtable[level].append(node.val)
        if node.left:
            self.dfs(node.left, level+1, hashtable)
        if node.right:
            self.dfs(node.right, level+1, hashtable)
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        