
success = ["6/27"]
"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins2(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        depth_map = {}
        stack = [(root, None, 0)]

        while stack:
            node, parent, dep = stack.pop()
            if node is not None:
                depth_map[node.val] = [parent, dep]
                stack.append((node.left, node, dep+1))
                stack.append((node.right, node, dep+1))

        return (depth_map[x][1] == depth_map[y][1]) and (depth_map[x][0] != depth_map[y][0])
        

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        queue = deque()
        queue.append((root, None, 0))
        results = []

        while queue:
            node, parent, depth = queue.popleft()
            if node is not None:
                if node.val in {x, y}:
                    results.append((parent, depth))
                    if len(results) == 2:
                        break
                queue.append((node.left, node, depth+1))
                queue.append((node.right, node, depth+1))

        node_x, node_y = results
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
                

            