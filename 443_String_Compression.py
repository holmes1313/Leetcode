# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:04:31 2019

@author: z.chen7
"""

# 443. String Compression
"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 

Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
 

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
"""
import collections

def compress(chars):
    """
    :type chars:List[str]
    :rtype: int
    """
    result = ""
    counts = collections.Counter(chars)
    unique_letters = []
    for letter in unique_letters:
        if letter not in unique_letters:
            unique_letters.append(letter)
    
    for letter in unique_letters:
        count = str(counts[letter]) if counts[letter] > 1 else ""
        result += letter
        result += count
    chars[:] = list(result)
    return len(chars)
    



chars = ["a","a","a","b","b","a","a"]
result = ""
counts = collections.Counter(chars)
unique_letters = []
for letter in chars:
    if letter not in unique_letters:
        unique_letters.append(letter)
unique_letters
counts

for letter in unique_letters:
    count = str(counts[letter]) if counts[letter] > 1 else ""
    result += letter
    result += count
result

chars[:] = list(result)
chars    




counts = collections.Counter(["a","a","b","b","c","c","c"])
counts
result = ""
for letter, count in counts.items():
        count = str(count) if count > 1 else ""
        result += letter
        result += count
list(result)
