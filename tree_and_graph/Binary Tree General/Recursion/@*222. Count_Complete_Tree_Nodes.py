"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    perfect binary tree's nodes amount
    2 ** (height) - 1

    Geometric progression
    an = a1 * q**(n-1)
    sn = a1 * (1-q**n)/(1-q)

    """
    def countNodes(self, root):
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        if not root:
            return 0

        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if left_height == right_height:
            # left sub is a perfect tree
            return 1 + (2 ** left_height - 1) + self.countNodes(root.right)
        else:
            # right tree is a perfect tree
            return 1 + self.countNodes(root.left) + (2 ** right_height - 1)
