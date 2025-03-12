"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        
        stack = [(root, 0, {0: 1})]
        total_paths = 0

        while stack:
            node, prefix_sum, prefix_sum_counts = stack.pop()

            prefix_sum += node.val

            if prefix_sum - targetSum in prefix_sum_counts:
                total_paths += prefix_sum_counts[prefix_sum - targetSum]
            
            if prefix_sum in prefix_sum_counts:
                prefix_sum_counts[prefix_sum] += 1
            else:
                prefix_sum_counts[prefix_sum] = 1

            # The dictionary is mutable, so if you pass it into the stack, the same dictionary is shared across all nodes. 
            # This means that when you update prefix_sums for one node, it is also updated for all other nodes, which could lead to incorrect results.
            # To fix this issue, you need to make sure that each node has its own separate copy of the prefix_sums dictionary, 
            # which is crucial to ensure that the prefix sums are correctly tracked for each path independently.
            if node.left:
                stack.append((node.left, prefix_sum, prefix_sum_counts.copy()))
            
            if node.right:
                stack.append((node.right, prefix_sum, prefix_sum_counts.copy()))

        return total_paths
