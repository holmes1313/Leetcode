# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:18:30 2019

@author: z.chen7
"""
# 257. Binary Tree Paths
"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):    
    
    # DFS (queue)
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []    
        result = []
        stack = [(root, '')]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                result.append(path + str(node.val))
            else:
                path = path + str(node.val) + '->'
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))
        return result


    # depth first search (recursively)
    def binaryTreePaths2(self, root):
        if not root:
            return []        
        result = []
        self.dfs(root, "", result)
        return result
        
    def dfs(self, node, path, result):
        if not node.left and not node.right:
            result.append(path + str(node.val))
        else:
            path = path + str(node.val) + '->'
            if node.left:
                self.dfs(node.left, path, result)            
            if node.right:
                self.dfs(node.right, path, result)
                
            