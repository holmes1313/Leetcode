"""

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = list(str(n))
        n = len(digits)

        # 1.find the pivot
        # Starting from the rightmost end, find the first pair of adjacent digits where the left digit is smaller than the right digit. 
        pivot = -1
        for  i in range(n - 2, -1, -1):
            if digits[i] < digits[i+1]:
                pivot = i
                break
        # If no pivot found, this is the highest permutation
        if pivot == -1:
            return -1
        
        # 2. find the successor and swap with pivot
        # From the right end, find the smallest digit that is larger than the pivot digit.
        for i in range(n-1, pivot, -1):
            if digits[i] > digits[pivot]:
                digits[i], digits[pivot] = digits[pivot], digits[i]
                break

        # 3. Reverse the Suffix
        # Reverse the sequence of digits to the right of the pivot position to get the smallest possible order.
        digits = digits[:pivot+1] + digits[pivot+1:][::-1]

        ans = int("".join(digits))

        if ans > 2 ** 31 - 1:
            return -1

        return ans
