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










# 20. Valid Parentheses
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
def isValid(s):
     """
     :type s: str
     :rtype: bool
     """
     while ('()' in s) or ('{}' in s) or ('[]' in s):
         s = s.replace('()', '').replace('[]', '').replace('{}', '')
         
    return s == ''



# 13. Roman to Integer
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""

"""
bad answer
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum_no = 0
    
    combos = {"IV": 4,
     "IX": 9,
     "XL": 40,
     "XC": 90,
     "CD": 400,
     "CM": 900}

    symbols = {"I": 1,
     "V": 5,
     "X": 10,
     "L": 50,
     "C": 100,
     "D": 500,
     "M": 1000}
    

    for combo in combos:
        while combo in s:
            s = s.replace(combo, "", 1)
            sum_no += combos[combo] 
            
    for symbol in symbols:
        while symbol in s:
            s = s.replace(symbol, "", 1)
            sum_no += symbols[symbol]
    
    return sum_no
"""

def romanToInt(s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    sum_amount = 0
    
    for i in range(len(s)-1):
        if roman[s[i]] < roman[s[i+1]]:
            sum_amount -= roman[s[i]]
        else:
            sum_amount += roman[s[i]]
            
    return sum_amount + roman[s[-1]]
            
    

# 21. Merge Two Sorted Lists
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
        
    




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
        


# 88. Merge Sorted Array
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]"""

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype void Do not return anything, modifying nums1 in-place instead
    """
    #  nums1[m:m+n] = nums2[:n]
    # nums1.sort()
    
    # make a copyt of nums1
    nums1_copy = nums[:m]
    nums1[:] = []
    
    p1 = 0
    p2 = 0
    
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1
        
    if p1 < m:
        nums1[p1+p2:] = nums1_copy[p1:]
    else:
        nums1[p1+p2:] = nums2[p2:]

    
    
    










# 104. Maximum Depth of Binary Tree
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."""
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    ld = maxDepth(root.left)
    rd = maxDepth(root.right)
    return max(ld, rd) + 1



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
