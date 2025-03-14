"""
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
Example 3:

Input: s = "zzzzz"
Output: 15
 

Constraints:

1 <= s.length <= 105
s consists of lowercase letters.
"""
import collections


class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        n = len(s)
        counts = collections.Counter()
        start = 0
        ans = 0
        for i in range(n):
            counts[s[i]] += 1

            while len(counts) > 1 and start <= i:
                counts[s[start]] -= 1
                if counts[s[start]] == 0:
                    del counts[s[start]]
                start += 1

            ans += i - start + 1

        return ans % mod

    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        curr = 1
        n = len(s)
        total = 0
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr += 1
            else:
                total += (curr + 1) * curr // 2
                curr = 1
        total += (curr + 1) * curr // 2
        return total % mod
