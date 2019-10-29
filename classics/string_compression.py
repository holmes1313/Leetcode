# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:12:33 2019

@author: z.chen7
"""

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
    return chars


def compress_2(chars):
    index = 0
    result = []
    while index < len(chars):
        char = chars[index]
        count = 0
        while index < len(chars) and chars[index] == char:
            count += 1
            index += 1
        result.append(char)
        if count > 1:
            result.append(str(count))
        
    return len(''.join(result))

input = ["a","a","b","b","c","c","c", 'd', 'e', 'e', 'e','e','e','e','e','e','e', 'e','e']
compress_2(input)



"""
Given an array of characters, find the longest chunk of same consecutive character
and return (starting_index, length)


Input: 'abbbbaabb'
Output: (1, 4)
"""

def findLongestChunk(word):
    index = 0
    sub_index = 0
    result = []
    
    while index < len(word):
        count = 0
        char = word[index]
        
        while (index < len(word)) and (word[index] == char):
            count += 1
            index += 1
            
        result.append((sub_index, count))
        sub_index = index
        
    return sorted(result, key=lambda kv: kv[1] - kv[0])[-1]
            


"""
Given a list of integers, return the length of the longest sequence of consecutive numbers, 
e.g.:
input: [1, 2, 3, 5, 8, 9, 10, 11]
output: 4
"""

def longestConsecutiveNums(nums):
    if not nums:
        return 0    
    index = 0
    max_count = 1
    while index < len(nums) - 1:
        num = nums[index]
        count = 1
        while (index < len(nums) - 1) and (num == nums[index+1] - 1):
            count += 1
            index += 1
            num = nums[index]
        max_count = max(max_count, count)
        index += 1
    return max_count



a = [1, 2, 3, 5, 8, 9, 10, 11]
b = [1, 2, 3]
c = [1,2 , 5, 6, 7, 10, 11, 12, 13]
