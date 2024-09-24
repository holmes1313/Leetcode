"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        stack = []
        stack.append((root, 0))
        output = 0
        while stack:
            node, length = stack.pop()
            if node is not None:
                length += 1
                if not node.children:
                    output = max(output, length)
                    continue

                for child in node.children:
                    stack.append((child, length))

        return output