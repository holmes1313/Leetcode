"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 """

 """
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth1(self, root: 'Node') -> int:

        if root is None:
            return 0
        elif not root.children:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]

        return max(height) + 1

    def maxDepth2(self, root: 'Node') -> int:

        stack = []
        depth = 0
        if root is not None:
            stack.append((1, root))

        while stack:
            current_path, node = stack.pop()
            if not node.children:
                depth = max(depth, current_path)
                continue
            for c in node.children:
                stack.append((current_path+1, c))

        return depth


    def maxDepth3(self, root: 'Node') -> int:

        queue = deque()
        depth = 0
        if root is not None:
            queue.append((1, root))

        while queue:
            current_path, node = queue.popleft()
            if not node.children:
                depth = max(depth, current_path)
                continue
            for c in node.children:
                queue.append((current_path+1, c))

        return depth

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
                if not node.children:
                    output = max(output, length+1)

                for child in node.children:
                    stack.append((child, length+1))

        return output