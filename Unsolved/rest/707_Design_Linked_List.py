# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:15:52 2019

@author: z.chen7
"""

# 707. Design Linked List

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        curr = self.head
        for i in range(index):
            if curr:
                curr = curr.next
            else:
                return -1
        if curr:
            return curr.val
        else:
            return -1
                
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)    
        if not self.head:
            self.head = newNode
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        
        if index < 0:
            index = 0
        
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        if not self.head and index > 0:
            return
        curr = self.head
        for i in range(index-1):
            if curr:
                curr = curr.next
            else:
                return
        newNode.next = curr.next
        curr.next = newNode
            
            
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0:
            return
        
        if index == 0:
            self.head = self.head.next
            return 
        
        curr = self.head
        for i in range(1, index):
            if curr:
                curr = curr.next
            else:
                return
        if curr and curr.next:
            curr.next = curr.next.next
            
            
        
'''
# test1
obj = MyLinkedList()
obj.addAtHead(1)
obj.head.val
obj.addAtTail(3)
obj.head.next.val
obj.addAtIndex(1, 2)
obj.get(1)
obj.deleteAtIndex(1)
obj.get(1)


# test2
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtIndex(1, 2)
obj.get(1)
obj.get(0)
obj.get(2)


# test3
obj = MyLinkedList()
obj.get(0)
obj.addAtIndex(1, 2)
'''

# test4
def test1():
    obj = MyLinkedList()
    obj.get(1)
    obj.addAtIndex(1, 2)
    obj.get(0)
    obj.get(1)
    obj.addAtIndex(0, 1)
    obj.get(0)
    obj.get(1)
