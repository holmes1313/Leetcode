# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:45:29 2019

@author: z.chen7
"""

# 234. Palindrome Linked List
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?"""

# Reversing a singly linked list requires writing to O(n) memory space, 
# thus the space complexities for all "reverse-the-list"-based approaches are O(n), not O(1).

# reverse a list
# deque.popleft(), deque.pop()
# how to get midpoint of a linked list


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # find the middle node
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # compare the first and second half nodes
        while prev:
            if head.val != prev.val:
                return False
            prev = prev.next
            head = head.next
        return True


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1(object):
    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals == vals[::-1]


    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        second_half_start = self.start_of_second_half(head)
        second_half_start_reversed = self.reverse_list(second_half_start)
        
        first_position = head
        second_position = second_half_start_reversed
        while second_position:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next

        return True

    def start_of_second_half(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev