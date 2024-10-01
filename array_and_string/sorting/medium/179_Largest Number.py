"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
import functools


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            if x + y > y + x:
                return -1 # x should come before y
            elif x + y < y + x:
                return 1
            else:
                return 0

        nums_str = list(map(str, nums))
        # The cmp_to_key function in Python is used to convert a comparison function (which takes two arguments and returns a negative, zero, or positive value) into a key function (which takes a single argument and returns a value). 
        nums_str.sort(key=functools.cmp_to_key(compare))

        if nums_str[0] == "0":
            return "0"

        return "".join(nums_str)