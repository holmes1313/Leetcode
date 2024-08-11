"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

class Solution(object):
    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mapping = {}
        mapping2 = {}
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i]

            if t[i] in mapping2:
                if mapping2[t[i]] != s[i]:
                    return False
            else:
                mapping2[t[i]] = s[i]
        return True

    # first occurence transformation
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.transformString(s) == self.transformString(t)

    def transformString(self, s):
        first_occur_index = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in first_occur_index:
                first_occur_index[c] = str(i)
            new_str.append(first_occur_index[c])
        
        return " ".join(new_str)