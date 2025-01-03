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
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))

        last_index = {int(digit): i for i, digit in enumerate(num_list)}

        for i, digit in enumerate(num_list):
            for d in range(9, int(digit), -1):
                if d in last_index and last_index[d] > i:
                    num_list[i], num_list[last_index[d]] = num_list[last_index[d]], num_list[i]
                    return int("".join(num_list))

        return num
