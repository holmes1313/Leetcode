"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy1 = ListNode()
        dummy2 = ListNode()
        c1 = dummy1
        c2 = dummy2
        curr = head
        idx = 0
        while curr:
            if idx % 2 == 0:
                c1.next = curr
                c1 = c1.next
            else:
                c2.next = curr
                c2 = c2.next
            curr = curr.next
            idx += 1
        c2.next = None
        c1.next = dummy2.next
        return dummy1.next

        