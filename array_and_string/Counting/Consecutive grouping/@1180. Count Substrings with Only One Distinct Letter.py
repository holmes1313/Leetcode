"""
Given a string s, return the number of substrings that have only one distinct letter.

 

Example 1:

Input: s = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: s = "aaaaaaaaaa"
Output: 55
 

Constraints:

1 <= s.length <= 1000
s[i] consists of only lowercase English letters.
"""
class Solution(object):
    def countLetters(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = 1
        total = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                total += (1 + curr) * curr // 2
                curr = 1
        total += (1 + curr) * curr // 2
        return total
