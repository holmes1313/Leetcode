# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 21:21:33 2019

@author: z.chen7
"""

# 2. Add Two Numbers
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# linked list  +  string addition

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = current = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
                
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
                
            s = num1 + num2 + carry
            
            current.next = ListNode(s % 10)
            current = current.next    # ** let the linked list move on
            
            carry = s // 10
        
        return root.next  # * as the first node is 0
            
        
        
        
        
        
        
        
        
        