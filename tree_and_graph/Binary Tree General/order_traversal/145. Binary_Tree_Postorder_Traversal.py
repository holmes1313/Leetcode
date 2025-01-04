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
    def postorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if not node:
            return

        self.helper(node.left, result)
        self.helper(node.right, result)
        result.append(node.val)

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        vars = []
        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            vars.append(node.val)

        postorder(root)
        return vars