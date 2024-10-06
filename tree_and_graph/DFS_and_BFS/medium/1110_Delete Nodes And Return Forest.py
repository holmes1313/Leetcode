"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        stack = [root]
        to_delete_set = set(to_delete)
        tree = []
        while stack:
            node = stack.pop()
            if node:

                if node.left:
                    stack.append(node.left)
                    if node.left.val in to_delete_set:
                        node.left = None

                if node.right:
                    stack.append(node.right)
                    if node.right.val in to_delete_set:
                        node.right = None

                if node.val in to_delete_set:
                    if node.left is not None:
                        tree.append(node.left)

                    if node.right is not None:
                        tree.append(node.right)

        if root.val not in to_delete_set:
            tree.append(root)


        return tree

        