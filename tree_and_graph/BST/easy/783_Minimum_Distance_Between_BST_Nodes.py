# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:21:36 2019

@author: z.chen7
"""
# 783. Minimum Distance Between BST Nodes
"""
Given a Binary Search Tree (BST) with the root node root, return the minimum 
difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value is different.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# in-order traversal to sort the tree values
class Solution(object):
    def minDiffInBST(self, root):
        result = []
        self.dfs(root, result)
        min_diff = result[-1]  - result[0]
        for i in range(1, len(result)):
            min_diff = min(min_diff, result[i] - result[i-1])
        #print(result)
        return min_diff
        
    def dfs(self, node, result):
        if node.left:
            self.dfs(node.left, result)
            
        result.append(node.val)
        
        if node.right:
            self.dfs(node.right, result)
        

    
    
root1 = TreeNode(27)
root1.right = TreeNode(34)
root1.right.right = TreeNode(58)
root1.right.right.left = TreeNode(50)
root1.right.right.left.right = TreeNode(44)

root2 = TreeNode(90)
root2.left = TreeNode(69)
root2.left.left = TreeNode(49)
root2.left.right = TreeNode(89)
root2.left.left.right = TreeNode(52)

Solution().minDiffInBST(root1)
Solution().prev
Solution().result
Solution().diff
Solution().minDiffInBST(root2)
