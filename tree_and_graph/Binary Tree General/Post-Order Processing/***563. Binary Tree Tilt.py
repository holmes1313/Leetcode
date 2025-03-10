"""
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.

 

Example 1:


Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # we will traverse the tree in the post-order DFS
    # we visit a node's left and right subtrees before processing the value of the current node.
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total_tilt = [0]

        def calculate_sum(node):
            if not node:
                return 0

            left_sum = calculate_sum(node.left)
            right_sum = calculate_sum(node.right)

            tilt = abs(left_sum - right_sum)
            total_tilt[0] += tilt

            return left_sum + right_sum + node.val

        calculate_sum(root)
        return total_tilt[0]