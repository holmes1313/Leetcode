"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
"""
class Solution(object):
    def maximumSwap(self, num):

        nums = list(str(num))

        digit_idx = len(nums) - 1
        curr_largest_digit = int(nums[digit_idx])
        ans = num
        
        for i in range(len(nums)-2, -1, -1):
            if int(nums[i]) < curr_largest_digit:
                nums[i], nums[digit_idx] = nums[digit_idx], nums[i]
                ans = max(ans, int("".join(nums)))
                nums[i], nums[digit_idx] = nums[digit_idx], nums[i]
            elif int(nums[i]) > curr_largest_digit:
                digit_idx = i
                curr_largest_digit = int(nums[i])

        return ans

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))
        # Create a dictionary to store the last occurrence of each digit
        last_index = {int(digit): i for i, digit in enumerate(num_list)}

        for i, digit in enumerate(num_list):
            # Try to find a larger digit to swap with the current digit
            for d in range(9, int(digit), -1):
                if d in last_index and last_index[d] > i:
                    num_list[i], num_list[last_index[d]] = num_list[last_index[d]], num_list[i]
                    return int("".join(num_list))

        return num
