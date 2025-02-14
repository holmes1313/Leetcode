class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))

    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, low, high = stack.pop()

            if node:
                if node.val <= low or node.val >= high:
                    return False

                stack.append((node.left, low, node.val))
                stack.append((node.right, node.val, high))

        return True
