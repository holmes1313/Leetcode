"""
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

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
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        n = len(s)
        counter = collections.defaultdict(int)
        max_len = 0
        for i in range(n):
            counter[s[i]] += 1
            while counter[s[i]] > 2:
                counter[s[start]] -= 1
                start += 1

            max_len = max(max_len, i - start + 1)
        return max_len
