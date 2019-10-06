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









# * 53. Maximum Subarray
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""
nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    n = len(nums)
    curr_sum = max_sum = nums[0]
    
    for i in range(1, n):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
        
    return max_sum
        



    
    
    







# 121. Best Time to Buy and Sell Stock
"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0."""
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profix

maxProfit([7,1,5,3,6,4])
        
    
    
    
    
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit
    


# 125. Valid Palindrome
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false"""

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    if not s:
        return True
    
    string_s = ''.join(e for e in s if e.isalnum()).lower()
    return string_s == string_s[::-1]
    


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
    






# 344. Reverse String
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory."""
s = ["h","e","l","l","o"]
s[::-1]
s

def reserverString(string):
    """ Do not return anything, modify s in-place instead"""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
            
reserverString(s)
print(s)



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


# 937. Reorder Data in Log Files
"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 
Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 

Constraints:
0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""

def reorderLogFiles(logs):
    def f(log):
        id_, rest = log.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1, )
            
    return sorted(logs, key=f)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
log = logs[0]
log.split(" ")
id_, rest = log.split(" ", 1)
rest[0].isalpha()
