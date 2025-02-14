"""
https://www.1point3acres.com/bbs/thread-644592-1-1.html



follow-up:
can we do recursion?
what if the linked list represents a negative number?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            curr.next = ListNode(val % 10)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry

            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def helper(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            curr_node = ListNode(total % 10)
            next_node = helper(l1.next if l1 else None, l2.next if l2 else 0, total // 10)
            curr_node.next = next_node
            return curr_node

        return helper(l1, l2, 0)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        curr = dummy
        carry = 0
        sign1 = 1
        sign2 = 1

        if l1.val == "-":
            sign1 = -1
            l1 = l1.next

        if l2.val == "-":
            sign2 = -1
            l2 = l2.next

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = sign1 * val1 + sign2 * val2 + carry
            carry =  total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

