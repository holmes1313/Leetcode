"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if not node:
            return

        self.helper(node.left, result)
        self.helper(node.right, result)
        result.append(node.val)

    def postorderTraversal_iteration(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans[::-1]
