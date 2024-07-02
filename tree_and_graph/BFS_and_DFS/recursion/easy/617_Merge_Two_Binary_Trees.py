"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

 

Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
 
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees2(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 and not root2:
            return None

        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0

        root = TreeNode(v1+v2)
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root

    def mergeTrees3(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        
        stack = []
        stack.append((root1, root2))
        while stack:
            n1, n2 = stack.pop()
            if n1 is None and n2 is None:
                continue

            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            n1.val = v1 + v2

            stack.append((n1.left if n1 else TreeNode(0), n2.left if n2 else TreeNode(0)))
            stack.append((n1.right if n1 else TreeNode(0), n2.right if n2 else TreeNode(0)))


        return root1

    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2

        stack = []
        stack.append((root1, root2))

        while stack:
            n1, n2 = stack.pop()
            if n2 is None:
                continue

            n1.val += n2.val

            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))

            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))

        return root1

    def mergeTrees4(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2

        elif not root2:
            return root1

        else:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        
        return root

