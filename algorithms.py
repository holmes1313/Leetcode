# -*- coding: utf-8 -*-
"""
leetcode 

Algorithms

Created on Tue Sep 24 20:32:13 2019

@author: z.chen7
"""





# ??? 2. Add Two Numbers
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


  
  
# ??? 5. Longest Palindromic Substring
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

palindrome: a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""


s = 'babad'
ls = len(s)
ls

temp_s = '#'.join(s)

tls = len(temp_s)
tls
temp_s
















    


# ??? 146. LRU Cache
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4"""


# 155. Min Stack
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2."""
class MinStack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void"""
        self.stack.append((x, min(x, self.getMin())))
        
    def pop(self):
        """
        rtype: void"""
        self.stack.pop()
    
    def top(self):
        """
        :rtype: int"""
        return self.stack[-1][0]
    
    def getMin(self):
        """
        :rtype: int"""
        if self.stack:
            return self.stack[-1][1]
        return sys.maxint



# 202. Happy Number
"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1"""

def isHappy(n):
    """
    :type n: int
    :rtype bool
    """
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(d)**2 for d in str(n)])
    return n == 1
    
    
   

# ** 206. Reverse Linked List
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    https://www.youtube.com/watch?v=XDO6I8jxHtA
    """
    prev = None
    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev
    







# 771. Jewels and Stones
"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct."""

def numJewelsInStones(J, S):
    return sum([True for s in S if s in J])

numJewelsInStones("aA", S="aAAbbbb")


