"""
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.

 

Example 1:

Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
So the number of elements in the array with maximum frequency is 4.

Example 2:

Input: nums = [1,2,3,4,5]
Output: 5
Explanation: All elements of the array have a frequency of 1 which is the maximum.
So the number of elements in the array with maximum frequency is 5.
"""

class Solution2(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_freq = 0
        output = 0
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
            if counts[num] > max_freq:
                max_freq = counts[num]

        for freq in counts.values():
            if freq == max_freq:
                output += freq

        return output


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = 0
        max_count = 0
        count_map = collections.defaultdict(int)
        for num in nums:
            count_map[num] += 1
            
            if count_map[num] > max_freq:
                max_freq = count_map[num]
                max_count = 1
            elif count_map[num] == max_freq:
                max_count += 1

        return max_freq * max_count

        