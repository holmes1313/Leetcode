"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
"""
import collections


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cha_counts = collections.defaultdict(int)
        start = 0
        max_len = 0

        for end in range(len(s)):
            cha_counts[s[end]] += 1

            while True:
                max_freq = max(cha_counts.values())
                if (end - start + 1) - max_freq > k:
                    cha_counts[s[start]] -= 1
                    start += 1
                else:
                    break

            max_len = max(max_len, end - start + 1)

        return max_len
