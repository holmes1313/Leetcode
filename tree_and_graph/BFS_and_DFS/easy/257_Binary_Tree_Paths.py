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


class Solution:
    def binaryTreePaths2(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        ans = []
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                ans.append(path + f"{node.val}")
            if node.right:
                stack.append((node.right, path + f"{node.val}->"))
            if node.left:
                stack.append((node.left, path + f"{node.val}->"))

        return ans

    def binaryTreePaths3(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        ans = []
        self.helper(root, "", ans)
        return ans

    def helper(self, node, path, ans):
        if not node.left and not node.right:
            ans.append(path + f"{node.val}")

        if node.left:
            self.helper(node.left, path + f"{node.val}->", ans)

        if node.right:
            self.helper(node.right, path + f"{node.val}->", ans)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        stack = []
        stack.append((root, "")). # can't use changeable object like list
        while stack:
            node, path = stack.pop()
            if not node:
                continue
            path += str(node.val)
            if node.left is None and node.right is None:
                ans.append(path)
                continue

            stack.append((node.left, path+"->"))
            stack.append((node.right, path+"->"))

        return ans
