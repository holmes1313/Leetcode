"""
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

"""
class Solution(object):
    def minSwaps(self, data):
        """
        :type data: List[int]
        :rtype: int
        """
        # Count the total number of 1s in the array
        window_len = sum(data)
        # Initialize the window sum for the first 'total_ones' elements
        curr_window = sum(data[:window_len])
        # The minimum swaps needed will be based on the number of 0s in the initial window
        min_swaps = window_len - curr_window
        for i in range(window_len, len(data)):
            # Slide the window to the right
            curr_window += data[i] - data[i-window_len]
            # Calculate the number of swaps needed for the current window
            swaps = window_len - curr_window
            min_swaps = min(min_swaps, swaps)
        return min_swaps



