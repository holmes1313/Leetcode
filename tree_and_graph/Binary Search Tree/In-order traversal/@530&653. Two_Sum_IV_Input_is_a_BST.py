"""
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if k - node.val in self.seen:
                self.found = True
                return
            else:
                self.seen.add(node.val)

            inorder(node.right)

        self.seen = set()
        self.found = False
        inorder(root)
        return self.found
