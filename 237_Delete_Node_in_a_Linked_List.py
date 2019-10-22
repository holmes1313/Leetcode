# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:50:01 2019

@author: z.chen7
"""

# 237. Delete Node in a Linked List
"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function."""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(head, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    if head.val == node.val:
        
        head = head.next
        return head
    curr = head
    
    while curr and curr.next:
        if curr.next.val == node.val:
            curr.next = curr.next.next
            return head
        curr = curr.next
    

n1 = ListNode(4)
n2 = ListNode(5)
n3 = ListNode(1)
n4 = ListNode(9)

n1.next = n2
n2.next = n3
n3.next = n4

def test_1():
    deleteNode(n1, ListNode(4))




