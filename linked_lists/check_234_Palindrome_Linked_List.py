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
