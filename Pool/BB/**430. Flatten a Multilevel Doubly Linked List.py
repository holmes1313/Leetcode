

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        dummy = Node()
        curr = dummy
        
        stack = [head]
        while stack:
            node = stack.pop()

            curr.next = node
            node.prev = curr
            curr = curr.next

            if node.next:
                stack.append(node.next)

            if node.child:
                stack.append(node.child)
                node.child = None
        dummy.next.prev = None
        return dummy.next


