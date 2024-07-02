"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def increasingBST3(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        vals = []

        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        
        inorder(root)
        tree = TreeNode()
        curr = tree
        for val in vals:
            curr.right = TreeNode(val=val)
            curr = curr.right

        return tree.right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = curr = TreeNode(0)

        def inorder(node):
            if not node:
                return

            nonlocal curr
            inorder(node.left)
            new_node = TreeNode(node.val)
            curr.right = new_node
            curr = curr.right
            inorder(node.right)

        inorder(root)
        return head.right