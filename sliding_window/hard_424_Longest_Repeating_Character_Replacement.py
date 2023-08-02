"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

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
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ans = 0
        char_mapping = {}
        start = 0
        for idx, char in enumerate(s):

            if char not in char_mapping:
                char_mapping[char] = 1
            else:
                char_mapping[char] += 1

            max_count = max(char_mapping.values())
            if idx - start + 1 - max_count > k:   # key condition: window length - count of most frequent character < k
                char_mapping[s[start]] -= 1
                start += 1

            ans = max(ans, idx - start + 1)

        return ans
