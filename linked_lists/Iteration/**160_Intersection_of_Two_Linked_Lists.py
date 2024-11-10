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

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        
        # A and B will line up in the 2nd iteration: A+B & B+A
        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        
        return pA

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodes_in_B = set()

        while headB:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA:
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None