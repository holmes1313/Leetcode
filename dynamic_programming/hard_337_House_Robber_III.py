"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
"""
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        # return pair [withRoot, withoutRoot]
        def dfs(node):
            if not node:
                return [0, 0]

            left_pair = dfs(node.left)
            right_pair = dfs(node.right)

            withRoot = node.val + left_pair[1] + right_pair[1]
            withoutRoot = max(left_pair) + max(right_pair)

            return [withRoot, withoutRoot]

        return max(dfs(root))


# reference: https://www.youtube.com/watch?v=nHR8ytpzz7c
