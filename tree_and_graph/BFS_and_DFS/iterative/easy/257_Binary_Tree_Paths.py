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
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = [(root, "")]
        ans = []
        while stack:
            node, path = stack.pop()
            if node:
                if not path:
                    path = str(node.val)
                else:
                    path += "->" + str(node.val)
                if node.left is None and node.right is None:   # is node is leaf
                    ans.append(path)
                else:
                    stack.append((node.left, path))
                    stack.append((node.right, path))

        return [path for path in ans]

    def binaryTreePaths2(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        stack = [(root, str(root.val))]
        ans = []

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                ans.append(path)
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))

        return ans

        