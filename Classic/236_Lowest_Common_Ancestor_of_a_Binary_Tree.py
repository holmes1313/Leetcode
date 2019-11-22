# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:20:21 2019

@author: z.chen7
"""

# 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # check if p and q are descendants of the left subtree and the right subtree
        # if they are descendants of different subtrees, then the current node is the LCA
        # if they are descendants of the same subtree, then that subtree holds the LCA
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        else:
            return left or right




# Time Limt Exceed
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # check if p and q are descendants of the left subtree and the right subtree
        # if they are descendants of different subtrees, then the current node is the LCA
        # if they are descendants of the same subtree, then that subtree holds the LCA
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        pIsOnLeft = self.covers(root.left, p)
        qIsOnLeft = self.covers(root.left, q)
        
        print(pIsOnLeft)
        print(qIsOnLeft)
        
        if pIsOnLeft != qIsOnLeft:
            return root
        
        if pIsOnLeft:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        
        
    def covers(self, parent, child):
        if not parent:
            return False
        if parent.val == child.val:
            return True
        return self.covers(parent.left, child) or self.covers(parent.right, child)
        
    
node_3 = TreeNode(3)
node_5 = TreeNode(5)
node_1 = TreeNode(1)
node_3.left = node_5
node_3.right = node_1


Solution().lowestCommonAncestor(node_3, node_5, node_1)
Solution().covers(node_3.left, node_1)
node_3.left.val
