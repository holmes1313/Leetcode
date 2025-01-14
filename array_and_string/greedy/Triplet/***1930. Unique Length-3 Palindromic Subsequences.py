"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
"""
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        first_last_indices = {}
        for i, cha in enumerate(s):
            if cha not in first_last_indices:
                first_last_indices[cha] = [i, i]
            else:
                first_last_indices[cha][1] = i

        for key, val in first_last_indices.items():
            first_idx, last_idx = val
            if last_idx - first_idx > 1:
                for j in range(first_idx+1, last_idx):
                    seen.add(s[first_idx] + s[j] + s[last_idx])

        return len(seen)


    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        n = len(s)
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j] and j - i > 1:
                    for x in range(i+1, j):
                        seen.add(s[i]+s[x]+s[j])

        return len(seen)

    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set(s)
        ans = 0
        for cha in letters:
            i, j = s.index(cha), s.rindex(cha)
            between = set()

            for k in range(i+1, j):
                between.add(s[k])

            ans += len(between)

        return ans
