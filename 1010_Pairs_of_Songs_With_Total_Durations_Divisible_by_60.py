# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:36:24 2019

@author: z.chen7
"""
# 1010_Pairs_of_Songs_With_Total_Durations_Divisible_by_60
"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0. 

Example 1:
Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:
Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
"""



import collections

count = collections.Counter('aaabb')
count
count['c']
count.get('c', 0)

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256782/Detailed-Explanation-using-Modular-Arithmetic-C%2B%2BJavaScript-O(n)

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        mod_count = collections.Counter()
        
        for t in time:
            mod_count[t % 60] += 1
        
        # Now that we only have numbers from 0...59, 
        # let us see which numbers can sum up to zero.
        
        result = 0
        
        # Clearly each 0 can be paired with another zero to sum up to zero
        # How many ways are there to select? Clearly, nC2 = n*(n-1)/2
        if mod_count[0]:
            result += mod_count[0] * (mod_count[0] - 1) / 2
        
        # Clearly each 30 can be paired with another zero to sum up to zero
        # How many ways are there to select? Clearly, nC2 = n*(n-1)/2
        if mod_count[30]:
            result += mod_count[30] * (mod_count[30] - 1) / 2
        
        # We only loop upto 29 so as to avoid recounting. 
        # (Beacause every number greater than 30 has a complement less than 30, which has already been counted in the for loop).
        for mod in range(1, 30):
            result += mod_count[mod] * mod_count[60 - mod]
            
        return result