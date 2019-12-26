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

import collections

class Solution(object):
    # recursive
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)
        
    def dfs(self, node1, node2):
        if node1 and node2 and node1.val == node2.val:
            return self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)
        elif not node1 and not node2:
            return True
        else:
            return False
    
    # iterative
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        queue = collections.deque()
        queue.appendleft((root.left, root.right))
        
        while queue:
            l, r = queue.pop()
            
            if not l and not r:
                continue
            elif l and r and l.val == r.val:
                queue.appendleft((l.left, r.right))
                queue.appendleft((l.right, r.left))
            else:
                return False
        return True