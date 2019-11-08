# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:35:47 2019

@author: z.chen7
"""

# remove punctuations/spaces
re.findall('[a-zA-Z0-9]+', s)
# or 
[e for e in s if e.isalnum()]


# min len element
min(list, key=len)


# for...if...else 


# 198. House Robber
def rob_dp(nums):
    if len(nums) == 0:
        return 0
    a = 0
    b = nums[0]
    for i in range(1, len(nums)):
        temp = max(a + nums[i], b)
        a = b
        b = temp


# 206. Reverse Linked List
def reverseList(head):
    prev = None
    curr = head
    while curr:
        head = curr.next
        curr.next = prev
        prev = curr
        curr = head
    return prev


#* 21. Merge Two Sorted Lists
def mergeTwoLists(l1, l2):
    root = curr = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2
    return root.next


#* 234. Palindrome Linked List
# two pointers: fast and slow
def isPalindrome(head):
    fast = slow = curr =  head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.fast
        
    stack = []
    while slow:
        stack.append(slow.val)
        slow = slow.next
        
    while stack:
        if stack.pop() != curr.val:
            return False
        curr = curr.next
    return True


# 350. Intersection of Two Arrays II
import collections
def intersect(nums1, nums2):
    counts  = collections.Counter(nums1)
    result = []
    
    for num in nums2:
        if counts.get(num) > 0:
            counts[num] -= 1
            result.append(num)
            
    return result


# 387. First Unique Character in a String
import collections
def firstUniqChar(s):
    counts = collections.Counter(s)
    
    for i, v in enumerate(s):
        if counts[v] == 1:
            return i
        
    return -1


# * 415. Add Strings
import collections
def addStrings(num1, num2):

    num1 = list(num1)
    num2 = list(num2)
    carry = 0
    result = collections.deque()

    while num1 or num2 or carry:
        n1 = ord(num1.pop()) - ord('0') if num1 else 0
        n2 = ord(num2.pop()) - ord('0') if num2 else 0

        s = n1 + n2 + carry

        result.appendleft(s % 10)
        carry = s // 10

    return ''.join([str(n) for n in result])



# ** 443. String Compression
def compress(chars):
    index = subIndex = 0
    while index < len(chars):
        char = chars[index]
        count = 0
        while index < len(chars) and chars[index] == char:
            count += 1
            index += 1
        if count > 1:
            chars[subIndex+1: index] = str(count)
            index = subIndex + 2
        subIndex = index
    return len(chars)