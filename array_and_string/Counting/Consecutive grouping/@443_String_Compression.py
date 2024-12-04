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
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) < 2:
            return len(chars)
        next_idx = 0
        curr_count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                curr_count += 1
            else:
                chars[next_idx] = chars[i-1]
                next_idx += 1
                if curr_count > 1:
                    for digit in str(curr_count):
                        chars[next_idx] = digit
                        next_idx += 1
                curr_count = 1

        chars[next_idx] = chars[-1]
        next_idx += 1
        if curr_count > 1:
            for digit in str(curr_count):
                chars[next_idx] = digit
                next_idx += 1

        return next_idx

    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        next_idx = 0

        while i < len(chars):
            char = chars[i]
            curr_count = 0

            while i < len(chars) and chars[i] == char:
                curr_count += 1
                i += 1

            chars[next_idx] = char
            next_idx += 1

            if curr_count > 1:
                for digit in str(curr_count):
                    chars[next_idx] = digit
                    next_idx += 1

        return next_idx

    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) < 2:
            return len(chars)

        nxt_idx = 0
        curr_cha = chars[0]
        curr_count = 0
        for cha in chars:
            if cha == curr_cha:
                curr_count += 1
            else:
                chars[nxt_idx] = curr_cha
                nxt_idx += 1
                if curr_count > 1:
                    for digit in str(curr_count):
                        chars[nxt_idx] = digit
                        nxt_idx += 1
                curr_count = 1
                curr_cha = cha

        chars[nxt_idx] = curr_cha
        nxt_idx += 1
        curr_cha = cha
        if curr_count > 1:
            for digit in str(curr_count):
                chars[nxt_idx] = digit
                nxt_idx += 1
        return nxt_idx
