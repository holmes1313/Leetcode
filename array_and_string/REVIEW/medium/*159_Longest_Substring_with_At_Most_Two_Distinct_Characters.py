"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.



Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

"""
import collections


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0

        cha_counts = collections.defaultdict(int)
        for end in range(len(s)):
            cha_counts[s[end]] += 1

            while len(cha_counts.keys()) > 2 and start <= end:
                cha_counts[s[start]] -= 1
                if cha_counts[s[start]] == 0:
                    del cha_counts[s[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
            
