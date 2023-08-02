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

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        ans = 0
        index_mapping = {}
        start = 0

        for idx, char in enumerate(s):
            index_mapping[char] = idx
            if len(index_mapping) > k:
                temp = min(index_mapping.values())
                del index_mapping[s[temp]]
                start = temp + 1

            ans = max(ans, idx-start+1)

        return ans