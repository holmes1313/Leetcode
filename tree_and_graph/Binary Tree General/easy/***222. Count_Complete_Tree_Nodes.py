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
    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                count += 1
                stack.append(node.left)
                stack.append(node.right)

        return count

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def count_nodes_in_complete_tree(node):
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            # If the heights are equal, the left subtree is a perfect binary tree
            if left_height == right_height:
                return 2 ** left_height - 1 + count_nodes_in_complete_tree(node.right) + 1
            else:
                return count_nodes_in_complete_tree(node.left) + 2 ** right_height - 1 + 1

        return count_nodes_in_complete_tree(root)
                
