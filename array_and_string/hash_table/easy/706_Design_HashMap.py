# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:28:08 2019

@author: z.chen7
"""

# 706. Design HashMap
"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.
"""

class MyHashMap2(object):

    def __init__(self):
        self._map = {}
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self._map[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self._map.get(key, -1)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self._map:
            del self._map[key]
        

# hash function
# hash map
# linked list -> collision


class Node(object):
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap(object):    
    def __init__(self):
        """
        Initialize your data structure
        """
        self.bucket_number = 10000
        self.array = [None] * self.bucket_number
       
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        newNode = Node(key, value)
        index = self.calculate_hash_value(key)
        if not self.array[index]:
            self.array[index] = newNode
        else:
            curr = self.array[index]
            if curr.pair[0] == key:
                curr.pair = (key, value)
            else:
                while curr and curr.next:
                    if curr.next.pair[0] == key:
                        curr.next.pair = (key, value)
                        return
                    curr = curr.next
                curr.next = newNode  
    
    def get(self, key):
        """
        returns the value to which the specific key is mapped to, or -1 if 
        this map contains no mapping for the key.
        :type key: int
        :rtype: int
        """
        index = self.calculate_hash_value(key)
        curr = self.array[index]
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            curr = curr.next
        return -1
        
    def remove(self, key):
        """
        removes the mapping of the specified value key if map contains 
        a mapping for the key
        :type key: int
        """
        index = self.calculate_hash_value(key)
        curr = self.array[index]
        if curr and curr.pair[0] == key:
            self.array[index] = curr.next
            return
        while curr and curr.next:
            if curr.next.pair[0] == key:
                curr.next = curr.next.next
            curr = curr.next

    def calculate_hash_value(self, key):
        return key % self.bucket_number

