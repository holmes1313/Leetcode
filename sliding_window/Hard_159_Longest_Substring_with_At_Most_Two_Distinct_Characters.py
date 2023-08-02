"""
Given a string s, return the length of the longest
substring
 that contains at most two distinct characters.



Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct2(self, s: str) -> int:
        max_len = 0
        left = right = 0
        index_map = {}
        while right < len(s):
            index_map[s[right]] = right
            if len(index_map) > 2:
                del_index = min(index_map.values())
                del index_map[s[del_index]]
                left = del_index + 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len = 0
        start = 0
        index_map = {}
        for i, letter in enumerate(s):
            index_map[letter] = i
            if len(index_map) > 2:
                del_index = min(index_map.values())
                del index_map[s[del_index]]
                start = del_index + 1
            max_len = max(max_len, i - start + 1)
        return max_len
