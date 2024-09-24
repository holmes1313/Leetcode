"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
 
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_values = []
        stack = []
        stack.append(root1)
        while stack:
            node = stack.pop()
            if node is not None:
                if node.left is None and node.right is None:
                    leaf_values.append(node.val)

                stack.append(node.left)
                stack.append(node.right)

        leaf_values2 = []
        stack2 = []
        stack2.append(root2)
        while stack2:
            node = stack2.pop()
            if node is not None:
                if node.left is None and node.right is None:
                    leaf_values2.append(node.val)

                stack2.append(node.left)
                stack2.append(node.right)


        return leaf_values == leaf_values2


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def inorder(node, seq):
            if not node:
                return
            inorder(node.left, seq)
            if node.left is None and node.right is None:
                seq.append(node.val)
            inorder(node.right, seq)

        seq1 = []
        seq2 = []
        inorder(root1, seq1)
        inorder(root2, seq2)
        return seq1 == seq2

            

