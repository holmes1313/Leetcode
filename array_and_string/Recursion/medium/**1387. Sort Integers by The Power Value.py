"""
The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

if x is even then x = x / 2
if x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the kth integer in the range [lo, hi] sorted by the power value.

Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in a 32-bit signed integer.

 

Example 1:

Input: lo = 12, hi = 15, k = 2
Output: 13
Explanation: The power of 12 is 9 (12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1)
The power of 13 is 9
The power of 14 is 17
The power of 15 is 17
The interval sorted by the power value [12,13,14,15]. For k = 2 answer is the second element which is 13.
Notice that 12 and 13 have the same power value and we sorted them in ascending order. Same for 14 and 15.
Example 2:

Input: lo = 7, hi = 11, k = 4
Output: 7
Explanation: The power array corresponding to the interval [7, 8, 9, 10, 11] is [16, 3, 19, 6, 14].
The interval sorted by power is [8, 10, 11, 7, 9].
The fourth number in the sorted array is 7.
 

Constraints:

1 <= lo <= hi <= 1000
1 <= k <= hi - lo + 1
"""
class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        def get_power(n):
            power = 0
            while n != 1:
                power += 1
                if n % 2 == 0:
                    n //= 2
                else:
                    n = 3 * n + 1

            return power
        nums = [num for num in range(lo, hi+1)]
        nums.sort(key=lambda x: (get_power(x), x))

        return nums[k-1]

    def getKth(self, lo, hi, k):
        # Memoization dictionary to store previously computed powers
        cache = {}

        # Function to calculate the power of a number using recursion
        def calc_power(n):
            # If n is already computed, return the cached value
            if n in cache:
                return cache[n]
            
            # Base case: power of 1 is 0
            if n == 1:
                cache[n] = 0
                return 0
            
            # Base case: power of 2 is 1
            if n == 2:
                cache[n] = 1
                return 1
            
            # If n is even, calculate power recursively
            if n % 2 == 0:
                cache[n] = 1 + calc_power(n // 2)
            else:
                # If n is odd, calculate power recursively
                cache[n] = 1 + calc_power(3 * n + 1)
            
            return cache[n]

        # Create a list of numbers from lo to hi
        my_list = [i for i in range(lo, hi + 1)]

        # Sort the list by power and by number itself in case of ties
        my_list.sort(key=lambda x: (calc_power(x), x))

        # Return the k-th number (1-indexed, so k-1 for 0-indexed lists)
        return my_list[k - 1]
