# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:40:17 2019

@author: z.chen7
"""
# 160. Intersection of Two Linked Lists
"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Example
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not 
be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. 
From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the 
intersected node in A; There are 3 nodes before the intersected node in B.

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    a, b = headA, headB
    len_a, len_b = 0, 0
    while a:
        len_a += 1
        a = a.next
    while b:
        len_b += 1
        b = b.next
    
    a, b = headA, headB
    if len_a > len_b:
        for i in range(len_a - len_b):
            a = a.next
    else:
        for i in range(len_b - len_a):
            b = b.next
    
    while a != b:
        a = a.next
        b = b.next
    
    return a    



# answer solution
def getIntersectionNode_2(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    pa, pb = headA, headB  # two pointers
    
    # if either pointer hits the end, switch head and continue the second traversal, 
    # only 2 ways to get out of the loop, they meet or the both hit the end=None
    while pa is not pb:
        pa = pa.next if pa else headB   # can't be if pa.next then it will be infinite loop if there's no overlapping
        pb = pb.next if pb else headA
    
    return pa  
    
