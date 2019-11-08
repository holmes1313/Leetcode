# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:36:30 2019

@author: z.chen7
"""

# Kanerai 

# Q1
"""
Write the function that takes a list of paths and returns the number of unique directories. 
Each path always starts with “/”.
If the path ends with “/”, it’s a directory. Otherwise it’s a regular file.
For example if arr is ["/a/b/","/x/y"] the function returns 4 because there are 5 unique directories: "/", "/a", "a/b", "/x"
"""
def uniqueDirect(paths):
   result = ['/']
   for path in paths:
       helper(path, [], result)
   return result

def helper(path, curr, result):
    while path.rfind('/'):
        result.append(path[:path.rfind('/')])
        path = path[:path.rfind('/')]


# Q2
"""
Write a function RangeSize that given a range reference in a 2d table, 
returns the number of cells in that range
The column headers are specified using only 4 uppercase letters, A, B, C and D 
(not the entire 26 letters of the alphabet). 
The columns start with ‘A’, ‘B’, ‘C’, ‘D’, then ‘AA’, ‘AB’, …, ‘DD’, then ‘AAA’, … The total number of rows cannot exceed 10,000.
The row headers are positive integers, starting from 1, 2, … . The total number of rows cannot exceed 1,000,000
A cell reference can be specified as <columnheader><rowheader> where the column header needs to come before the row header. 
For example, AB23 refers to column AB and row 23.

A range reference can be specified using the cell reference fo the upper left corner and the cell reference of the bottom right corner.
For example:
·         A1:C2 has 6 cells, including A1, A2, B1, B2, C1, C2.
·         A1:AA2 has 10 cells, including A1, A2, B1, B2, C1, C2, D1, D2, AA1, AA2.
If a range reference is invalid, -1 should be returned.
Test cases include both valid and invalid range references.
"""


class Solution(object):
    def colToNum(self, col):
        num = 0
        for chr in col:
            if chr.isalpha():
                num = num * 4 + (ord(chr.upper()) - ord('A')) + 1
        return num
    
    def cellToValue(self, cell):
        for i in range(len(cell)):
            if not cell[i].isalpha():
                col = cell[:i]
                row = cell[i:]
                break
        col_val = self.colToNum(col)
        row_val = int(row)
        return (col_val, row_val)
    
    def rangeSize(self, input1):
        left, right = input1.split(':')
        left_loc = self.cellToValue(left)
        right_loc = self.cellToValue(right)
    
        if left_loc[0] > right_loc[0] or left_loc[1] > right_loc[1]:
            return -1
        
        return (right_loc[0] - left_loc[0] + 1) * (right_loc[1] - left_loc[1] + 1)
    
Solution().rangeSize('A1:C3')
Solution().rangeSize('A1:AA2')
Solution().rangeSize('AA1:A2')



# Q3
"""
Write a function that takes the array of numbers which will contain the initial stock price, 
and the changes to the price in subsequent trading days. 
For example, if array is [30, -1, -1, -2, 1, -3], the initial stock price line is 30, 
and subsequent changes are -1, -1, -2, 1 and -3 (the corresponding prices are 26, 28, 26, 27 and 24 respectively). 
If the cumulative loss is greater than or equal to 5.00% (round to 2 decimal points) between trading days x, y where x<y , 
we call the period between the two trading days a “bad period”.

to return the number of bad periods
[30, -1, -1, -2, 1, -3] there priods 0 -> 2, 2->3, 4 -> 5
"""

def countBadPeriods(prices):
    price = prices[0]
    result = 0
    for chg in prices[1:]:
        if (chg / price) <= -0.05:
            result += 1
            price += chg
    return result


countBadPeriods([30, -1, -2, -4, -3, -6])

-1 / 30
-2 / 30
-4 / 28
-3 / 26
-6 / 23
