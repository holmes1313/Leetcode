# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:46:38 2019

@author: z.chen7
"""

# Recursively remove all adjacent duplicates
"""
Given a string, recursively remove adjacent duplicate characters from the string. The output string should not have any adjacent duplicates. See following examples.
Examples:

Input: azxxzy
Output: ay
First “azxxzy” is reduced to “azzy”.
The string “azzy” contains duplicates,
so it is further reduced to “ay”.



Input: geeksforgeeg
Output: gksfor
First “geeksforgeeg” is reduced to
“gksforgg”. The string “gksforgg”
contains duplicates, so it is further
reduced to “gksfor”.

Input: caaabbbaacdddd
Output: Empty String

Input: acaaabbbacdddd
Output: acac"""


def removeAdjacentDups(word):
    
    index = subIndex = 0
    words = list(word)
    
    for i in range(len(word)):
        while index < len(words):
            chr = words[index]
            count = 0
            while index < len(words) and chr == words[index]:
                count += 1
                index += 1
            
            if count > 1:
                words[subIndex: index] = ''
                index -= count
            subIndex = index
                
    return words
    
    
    
# Find the minimum element in a sorted and rotated array
"""
A sorted array is rotated at some unknown point, find the minimum element in it.

Following solution assumes that all elements are distinct.
Examples:

Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1"""

def finMin(array):
    if len(array) == 2:
        return min(array)
    
    if len(array) > 2:
        for i in range(1, len(array) - 1):
            if (array[i] < array[i+1]) and (array[i] < array[i-1]):
                return min(array[0], array[-1], array[i])
            
        

# Median of two sorted arrays with different sizes in O(log(min(n, m)))
import collections

def getMedia(arr1, arr2):
    a = len(arr1) + len(arr2)
    
    dq1 = collections.deque(arr1)
    dq2 = collections.deque(arr2)
    result = []
    
    for k in range(a // 2 + 1):
        if dq1 and dq2:
            if dq1[0] < dq2[0]:
               result.append(dq1.popleft())
            else:
                result.append(dq2.popleft())
        
        elif dq1:
            result.append(dq1.popleft())
            
        else:
            result.append(dq2.popleft())
            
    if a % 2 == 0:
        return (result[-1] + result[-2]) / 2
    else:
        return result[-1]
    


def test1():
    import pdb;pdb.set_trace()
    aa = getMedia([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10])
    import pdb;pdb.set_trace()
    
    
            
# Arrange given numbers to form the biggest number | Set 1        


def arrangeBiggest(arr):
    arr_str = [str(a) for a in arr]
    longest = len(max(arr_str, key=len))
    
    
    k = {a: str(a) + '9' * (longest - len(str(a)) for a in arr}
    import pdb;pdb.set_trace()
    return ''.join([sorted(arr, key=lambda x: k.get(x), reverse=True)])



def test_2():
    import pdb;pdb.set_trace()
    aa = arrangeBiggest([54, 546, 548, 60])
    import pdb;pdb.set_trace()
    bb = arrangeBiggest([1, 34, 3, 98, 9, 76, 45, 4])
    import pdb;pdb.set_trace()
    














