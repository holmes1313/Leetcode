# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:00:06 2019

@author: z.chen7
"""

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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val == n2.val and dfs(n1.left, n2.right) and dfs(n1.right, n2.left)
        
        return dfs(root.left, root.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        queue = collections.deque([(root.left, root.right)])

        while queue:
            n1, n2 = queue.popleft()

            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False

            queue.append((n1.left, n2.right))
            queue.append((n1.right, n2.left))

        return True 
