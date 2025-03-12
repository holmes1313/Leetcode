"""
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

 

Example 1:


Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.
Example 2:


Input: tree = [7], target =  7
Output: 7
Example 3:


Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        stack = [(original, cloned)]
        while stack:
            n1, n2 = stack.pop()

            if n1:
                if n1 == target:
                    return n2
                
                stack.append((n1.left, n2.left))
                stack.append((n1.right, n2.right))

    def getTargetCopy(self, original, cloned, target):
        if not original:
            return None

        if original == target:
            return cloned

        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result
        
        return self.getTargetCopy(original.right, cloned.right, target)
