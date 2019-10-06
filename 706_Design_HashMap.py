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
        self.bucket_number = 1000
        self.hashmap = [None] * self.bucket_number
    
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = self.calculate_hash_value(key)
        if self.hashmap[index] == None:
            self.hashmap[index] = Node(key, value)
        else:
            current = self.hashmap[index]
            while current:
                if current.pair[0] == key:
                    current.pair = (key, value)
                    return
                if current.next:  
                    current = current.next
                else:
                    break
            current.next = Node(key, value)
    
    def get(self, key):
        """
        returns the value to which the specific key is mapped to, or -1 if 
        this map contains no mapping for the key.
        :type key: int
        :rtype: int
        """
        index = self.calculate_hash_value(key)
        current = self.hashmap[index]
        
        while current:
            if current.pair[0] == key:
                return current.pair[1]
            current = current.next
            
        return -1
        
    def remove(self, key):
        """
        removes the mapping of the specified value key if map contains 
        a mapping for the key
        :type key: int
        """
        index = self.calculate_hash_value(key)
        prev = None
        current = self.hashmap[index]
        
        if not current:
            return
        
        while current.pair[0] != key and current.next:
            prev = current
            current = current.next
        
        if current.pair[0] == key:
            if prev:
                prev.next = current.next
                # self.hashmap[index] = prev (why we dont need this step)
            else:
                self.hashmap[index] = current.next
                # current = current.next (wrong)
        
    def calculate_hash_value(self, key):
        return key % self.bucket_number



hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.get(1)
hashMap.get(3)
hashMap.put(2, 1)
hashMap.get(2)
hashMap.remove(2)
hashMap.get(2)


hashMap = MyHashMap()
hashMap.put(1, 1)
hashMap.put(1001, 1001)
hashMap.put(1000001, 1000001)
hashMap.hashmap[1].next.next.pair

hashMap.remove(1001)
hashMap.hashmap[1].next.pair

hashMap.remove(1)
hashMap.hashmap[1].pair

hashMap.remove(1000001)
hashMap.hashmap[1].next.next.pair
