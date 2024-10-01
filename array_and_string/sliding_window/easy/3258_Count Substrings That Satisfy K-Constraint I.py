"""
You are given a binary string s and an integer k.

A binary string satisfies the k-constraint if either of the following conditions holds:

The number of 0's in the string is at most k.
The number of 1's in the string is at most k.
Return an integer denoting the number of 
substrings
 of s that satisfy the k-constraint.

 

Example 1:

Input: s = "10101", k = 1

Output: 12

Explanation:

Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.

Example 2:

Input: s = "1010101", k = 2

Output: 25

Explanation:

Every substring of s except the substrings with a length greater than 5 satisfies the k-constraint.

Example 3:

Input: s = "11111", k = 1

Output: 15

Explanation:

All substrings of s satisfy the k-constraint.
"""
import collections


class Solution(object):
    def countKConstraintSubstrings2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def is_k_constaint(s, k):
            counter = collections.Counter(s)
            return counter["1"] <= k or counter["0"] <= k
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                substr = s[i:j]
                if is_k_constaint(substr, k):
                    count += 1
                else:
                    break

        return count

    def countKConstraintSubstrings1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            zero_count = 0
            one_count = 0
            for j in range(i, len(s)):
                if s[j] == "0":
                    zero_count += 1
                else:
                    one_count += 1

                if zero_count <= k or one_count <= k:
                    count += 1
                else:
                    break
        return count

    def countKConstraintSubstrings1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        count = 0
        while start < len(s):
            end = start
            zero_count = 0
            one_count = 0
            while end < len(s):
                if s[end] == "0":
                    zero_count += 1
                else:
                    one_count += 1
                if zero_count <= k or one_count <= k:
                    count += 1
                end += 1
            start += 1
        return count

    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            counter = collections.defaultdict(int)
            for j in range(i, len(s)):
                counter[s[j]] += 1
                if  counter["1"] > k and counter["0"] > k:
                    break
                else:
                    ans += 1                 
        return ans

    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        n = len(s)
        for left in range(n):
            zeros = 0
            ones = 0
            right = left
            while right < n:
                if s[right] == "1":
                    ones += 1
                else:
                    zeros += 1
                
                if zeros <= k or ones <= k:
                    ans += 1
                else:
                    break

                right += 1

        return ans
