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
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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
        while l1 and l2:
            digit_sum = l1.val + l2.val + carry
            if digit_sum < 10:
                curr.next = ListNode(digit_sum)
                carry = 0
            else:
                curr.next = ListNode(digit_sum % 10)
                carry = 1
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            digit_sum = l1.val + carry
            if digit_sum < 10:
                curr.next = ListNode(digit_sum)
                carry = 0
            else:
                curr.next = ListNode(digit_sum % 10)
                carry = 1
            curr = curr.next
            l1 = l1.next

        while l2:
            digit_sum = l2.val + carry
            if digit_sum < 10:
                curr.next = ListNode(digit_sum)
                carry = 0
            else:
                curr.next = ListNode(digit_sum % 10)
                carry = 1
            curr = curr.next
            l2 = l2.next

        if carry:
            curr.next = ListNode(1)

        return dummy.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next    