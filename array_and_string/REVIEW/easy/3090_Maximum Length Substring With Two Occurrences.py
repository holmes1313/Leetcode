"""
Given a string s, return the maximum length of a 
substring
 such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

"""
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = right = 0
        ans = 0
        count_map = collections.defaultdict(int)
        while right < len(s):
            count_map[s[right]] += 1
            while count_map[s[right]] == 3:
                count_map[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1

        return ans
        