"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # In-Order Traversal: We can perform an in-order traversal (left, root, right) on the BST. Since the BST is ordered, an in-order traversal will visit the nodes in increasing order.
        # Track kth Node: As we traverse the tree, we can keep a count of how many nodes we've visited. When we reach the kth node, we return its value.

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # # Visit the current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            inorder(node.right)

        self.count = 0
        self.result = None
        inorder(root)
        return self.result

