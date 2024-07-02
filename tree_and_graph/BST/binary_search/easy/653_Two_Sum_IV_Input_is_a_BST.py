"""
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = collections.deque()
        queue.append(root)
        explored = set()

        while queue:
            node = queue.popleft()
            if node:
                if k - node.val in explored:
                    return True

                explored.add(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return False

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        vals = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)
        l = 0
        r = len(vals) - 1
        while l < r:
            curr_sum = vals[l] + vals[r]
            if curr_sum == k:
                return True

            if curr_sum < k:
                l += 1
            else:
                r -= 1
        return False

            


        
        