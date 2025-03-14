
"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        count = collections.defaultdict(int)

        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            count[node.val] += 1
            inorder(node.right)

        inorder(root)

        max_count = max(count.values())

        modes = [val for val, freq in count.items() if freq == max_count]

        return modes

    def findMode(self, root):
        if not root:
            return []

        def inorder(node):
            if not node:
                return 

            inorder(node.left)
            if self.prev is not None:
                if node.val == self.prev:
                    self.curr_count += 1
                else:
                    if self.curr_count > self.max_count:
                        self.max_count = self.curr_count
                        self.mode = [self.prev]
                    elif self.curr_count == self.max_count:
                        self.mode.append(self.prev)
                    self.curr_count = 1
            self.prev = node.val

            inorder(node.right)

        self.prev = None
        self.curr_count = 1
        self.max_count = 1
        self.mode = []

        inorder(root)

        if self.curr_count > self.max_count:
            self.max_count = self.curr_count
            self.mode = [self.prev]
        elif self.curr_count == self.max_count:
            self.mode.append(self.prev)

        return self.mode
