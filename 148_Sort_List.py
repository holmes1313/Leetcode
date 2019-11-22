# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:31:28 2019

@author: z.chen7
"""

# 148. Sort List
"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
(1) iterate LinkedList, add each node to a list
(2) sort the list 
(3) iterate the list and add each node to a new LinkedList
"""
class Solution1(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next
    
        self.mergeSort(array)
        
        newHead = curr1 = ListNode(0)
        for n in array:
            curr1.next = ListNode(n)
            curr1 = curr1.next
        return newHead.next
    
    def mergeSort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            
            self.mergeSort(left)
            self.mergeSort(right)
            
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1