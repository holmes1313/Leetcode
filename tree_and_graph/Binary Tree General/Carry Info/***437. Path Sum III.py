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
        
        stack = [(root, 0)]  # Each element is (node, current_sum)
        prefix_sums = {0: 1}  # Initialize with sum 0 seen once
        total_paths = 0

        while stack:
            node, current_sum = stack.pop()

            if node:
                # Update the current cumulative sum
                current_sum += node.val
                
                # Check if there's a path that sums to targetSum
                total_paths += prefix_sums.get(current_sum - targetSum, 0)

                # Update the prefix sums
                prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

                # Push right and left children to the stack
                stack.append((node.right, current_sum))
                stack.append((node.left, current_sum))

                # Backtrack: decrement the current sum count after processing the node
                # We do this after adding children to ensure we correctly count paths
                if prefix_sums[current_sum] > 1:
                    prefix_sums[current_sum] -= 1
                else:
                    del prefix_sums[current_sum]

        return total_paths
