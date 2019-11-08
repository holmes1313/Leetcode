# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:15:07 2019

@author: z.chen7
"""

# 101. Symmetric Tree
# *** recursion
"""
Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

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
 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""

class Solution(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        left = root.left
        right = root.right
        
        return self.helper(left, right)
        
    def helper(self, left, right):
        
        if not (left or right):
            return True
        
        elif left and right:
            
            if left.val != right.val:
                return False
            
            else:
                return (self.helper(left.left, right.right) & self.helper(left.right, right.left))
            
        else:
            return False
        
        

class Solution_2(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        left_path = []
        right_path = []
        self.dfs(root.left, left_path, True)
        self.dfs(root.right, right_path, False)
        print(left_path)
        print(right_path)
        return left_path == right_path
        
        
    def dfs(self, node, result, left):
        if not node:
            result.append('null')
            
        elif left:
            result.append(node.val)
            self.dfs(node.left, result, True)
            self.dfs(node.right, result, True)
        
        else:
            result.append(node.val)
            self.dfs(node.right, result, False)
            self.dfs(node.left, result, False)
        