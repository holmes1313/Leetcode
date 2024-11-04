# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:23:00 2020

@author: z.chen7
"""
# 434. Number of Segments in a String

"""
Count the number of segments in a string, where a segment is defined to be 
a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        
