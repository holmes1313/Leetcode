"""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        column_map = collections.defaultdict(list)

        stack = [(root, 0, 0)]

        while stack:
            node, row, col = stack.pop()

            if node:
                column_map[col].append((row, node.val))
                stack.append((node.right, row+1, col+1))
                stack.append((node.left, row+1, col-1))
        result = []
        for col in sorted(column_map.keys()):
            column_map[col].sort(key=lambda x: x[0])
            result.append([val for row, val in column_map[col]])

        return result

    def verticalOrder1(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        col_map = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])

        while queue:
            node, col = queue.popleft()
            if node:
                col_map[col].append(node.val)
                queue.append((node.left, col-1))
                queue.append((node.right, col+1))

        result = []
        for col in sorted(col_map.keys()):
            result.append(col_map[col])

        return result