"""

A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
"""
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = 3
        ans = 0
        for i in range(len(s)-k+1):
            substr = s[i:i+k]
            if len(set(substr)) == k:
                ans += 1

        return ans

    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        char_counts = collections.defaultdict(int)

        for i in range(len(s)):
            char_counts[s[i]] += 1

            if i >= 3:
                left_char = s[i-3]
                char_counts[left_char] -= 1
                if char_counts[left_char] == 0:
                    del char_counts[left_char]

            if i >= 2:
                if len(char_counts) == 3:
                    count += 1

        return count

