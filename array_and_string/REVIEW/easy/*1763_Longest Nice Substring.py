"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

"""

class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_nice(sub):
            seen_lower = set()
            seen_upper = set()

            for cha in sub:
                if cha.islower():
                    seen_lower.add(cha)
                elif cha.isupper():
                    seen_upper.add(cha.lower())

            return seen_upper == seen_lower

        n = len(s)
        longest = ""
        for start in range(n):
            for end in range(start+1, n+1):
                sub = s[start:end]
                if is_nice(sub):
                    if len(sub) > len(longest):
                        longest = sub

        return longest