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
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        results = []
        stack = [(root, 1, None)]
        while stack:
            node, depth, parent = stack.pop()
            if node:
                if node.val == x or node.val == y:
                    results.append((depth, parent))
                    if len(results) == 2:
                        break
                stack.append((node.left, depth+1, node))
                stack.append((node.right, depth+1, node))

        return results[0][0] == results[1][0] and results[0][1] != results[1][1]


    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False

        queue = collections.deque([(root, None)])  # (node, parent)

        while queue:
            size = len(queue)
            found_x = found_y = False
            parent_x = parent_y = None
            
            for _ in range(size):
                node, parent = queue.popleft()

                if node.val == x:
                    found_x = True
                    parent_x = parent
                elif node.val == y:
                    found_y = True
                    parent_y = parent

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            if found_x and found_y:
                return parent_x != parent_y
            if found_x or found_y:
                return False

        return False

