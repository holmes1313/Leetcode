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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
            """
        if not root:
            return []
        
        result = []  
        queue = deque([root])  
        left_to_right = True  
        
        while queue:
            level_size = len(queue) 
            level_nodes = [] 
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)  

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not left_to_right:
                level_nodes.reverse()

            result.append(level_nodes)
            
            left_to_right = not left_to_right
        
        return result