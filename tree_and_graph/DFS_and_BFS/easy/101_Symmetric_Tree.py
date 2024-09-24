REVIEW = ["6/27"]
# 101. Symmetric Tree
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 and node2 and node1.val == node2.val:
                return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
            else:
                return False

        return isMirror(root, root)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [(root, root)]
        while stack:
            node1, node2 = stack.pop()
            if node1 is None and node2 is None:
                continue
            if node1 and node2 and node1.val == node2.val:
                stack.append((node1.left, node2.right))
                stack.append((node1.right, node2.left))
            else:
                return False
        return True

