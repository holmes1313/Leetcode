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


class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    values = []
    current = head
    
    if not current:
        return True
    
    while current:
        values.append(current.val)
        current = current.next
    return values == reversed(values)
    

import collections

def isPalindrome_deque(head):
    queue = collections.deque([])
    current = head
    
    while current:
        queue.append(current.val)
        current = current.next
        
    while len(queue) >= 2:
        if queue.popleft() != queue.pop():
            return False
    return True


def isPalindrome_runner(head):
    if not (head and head.next):
        return True
    
    # 1. get the midpoint (slow)
    slow = fast = current = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # 2. push the second half to the stack (list)
    stack = []
    while slow:
        stack.append(slow.val)
        slow = slow.next
    
    # slow at the mid point
    
    # 3. comparison
    while stack:
        if stack.pop() != current.val:
            return False
        current = current.next
    
    return True
    
    
    
    