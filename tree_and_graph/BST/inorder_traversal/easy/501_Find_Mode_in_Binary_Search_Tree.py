
"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        mapping = collections.defaultdict(int)
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node is not None: 
                mapping[node.val] += 1

                stack.append(node.left)
                stack.append(node.right)

        max_feq = max(mapping.values())
        ans = []
        for key in mapping:
            if mapping[key] == max_feq:
                ans.append(key)

        return ans


# inorder solution
from typing import Optional, List


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []

        def inorder(node):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not node:
                return None

            inorder(node.left)

            num = node.val
            if node.val == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num

            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)

            inorder(node.right)

        inorder(root)
        return ans
        