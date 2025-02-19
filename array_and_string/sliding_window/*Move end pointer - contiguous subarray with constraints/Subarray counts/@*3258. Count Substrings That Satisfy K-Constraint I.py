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
        n = len(s)
        count = 0
        def is_k_constraint(sub):
            counter = collections.Counter(sub)
            if counter.get("1", 0) <= k or counter.get("0", 0) <= k:
                return True
            return False

        for start in range(n):
            for end in range(start+1, n+1):
                sub = s[start:end]
                if is_k_constraint(sub):
                    count += 1

        return count

    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        start = 0
        n = len(s)
        for start in range(n):
            end = start
            counter = {"1": 0, "0": 0}
            for end in range(start, n):
                counter[s[end]] += 1
                if counter["0"] <= k or counter["1"] <= k:
                    count += 1
                else:
                    break
        return count

    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ones = 0
        zeros = 0
        start = 0
        count = 0
        for end in range(len(s)):
            if s[end] == "0":
                zeros += 1
            else:
                ones += 1

            while ones > k and zeros > k:
                if s[start] == "0":
                    zeros -= 1
                else:
                    ones -= 1
                start += 1

            count += end - start + 1

        return count
