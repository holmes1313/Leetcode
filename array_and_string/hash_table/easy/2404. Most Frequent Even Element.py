"""
Given an integer array nums, return the most frequent even element.

If there is a tie, return the smallest one. If there is no such element, return -1.

 

Example 1:

Input: nums = [0,1,2,2,4,4,1]
Output: 2
Explanation:
The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
We return the smallest one, which is 2.
Example 2:

Input: nums = [4,4,4,9,2,4]
Output: 4
Explanation: 4 is the even element appears the most.
Example 3:

Input: nums = [29,47,21,41,13,37,25,7]
Output: -1
Explanation: There is no even element.

"""
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}

        most_freq = 0
        most_freq_num = -1

        for num in nums:
            if num % 2 != 0:
                continue

            counts[num] = counts.get(num, 0) + 1
            
            if counts[num] > most_freq:
                most_freq = counts[num]
                most_freq_num = num

            elif counts[num] == most_freq:
                most_freq_num = min(most_freq_num, num)

        return most_freq_num
