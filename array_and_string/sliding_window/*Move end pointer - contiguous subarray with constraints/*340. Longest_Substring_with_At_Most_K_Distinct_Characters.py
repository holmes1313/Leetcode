"""
Given a string s and an integer k, return the length of the longest
substring
 of s that contains at most k distinct characters.



Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

"""
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        max_len = 0
        cha_counts = collections.defaultdict(int)
        for end in range(len(s)):
            cha_counts[s[end]] += 1
            while len(cha_counts.keys()) > k:
                cha_counts[s[start]] -= 1
                if cha_counts[s[start]] == 0:
                    del cha_counts[s[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
