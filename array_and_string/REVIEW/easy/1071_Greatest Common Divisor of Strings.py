"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1 = len(str1) 
        l2 = len(str2)
        shortest = min(str1, str2, key=len)
        for i in range(len(shortest), 0, -1):
            divisor = shortest[:i]
            if l2 % len(divisor) == 0 and l2 % len(divisor) == 0:
                f1 = l1 // len(divisor)
                f2 = l2 // len(divisor)
                if divisor * f1 == str1 and divisor * f2 == str2:
                        return divisor
        return ""

