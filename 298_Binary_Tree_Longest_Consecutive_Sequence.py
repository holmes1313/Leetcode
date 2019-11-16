# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:17:26 2019

@author: z.chen7
"""

# 298. Binary Tree Longest Consecutive Sequence

"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in 
the tree along the parent-child connections. The longest consecutive path need 
to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""

# self solution

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = []
        self.helper(root, [], result)
        return max(result)
        
    def helper(self, node, current, result):
        if not current or node.val - 1 == current[-1]:
            current.append(node.val)
        else:
            result.append(len(current))
            current = [node.val]

        if not node.left and not node.right:
            result.append(len(current))
        if node.left:
            self.helper(node.left, current[:], result)
        if node.right:
            self.helper(node.right, current[:], result)
           
        
    