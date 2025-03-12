# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:40:33 2019

@author: z.chen7
"""

# 166. Fraction to Recurring Decimal

"""
Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

"""
Use HashMap to store a remainder and its associated index while doing the 
division so that whenever a same remainder comes up, we know there is a repeating fractional part.
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator / denominator)
        
        neg = False
        if numerator * denominator < 0:
            neg = True
            numerator = abs(numerator)
            denominator = abs(denominator)
            
        reminder = numerator % denominator
        integer = numerator / denominator
        reminders = {}
        remin_loc = 0
        decimals = ''
        while reminder and reminder not in reminders:
            reminders[reminder] = remin_loc
            remin_loc += 1
            decimals += str(reminder * 10 / denominator)
            reminder = reminder * 10 % denominator

        if reminder:
            rep_index = reminders[reminder]
            decimals = decimals[:rep_index] + '(' + decimals[rep_index:] + ')'
        return "-{}.{}".format(integer, decimals) if neg else "{}.{}".format(integer, decimals) 
        
        
        
       