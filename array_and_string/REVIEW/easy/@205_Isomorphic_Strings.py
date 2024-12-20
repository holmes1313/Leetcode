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
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for cha_s, cha_t in zip(s, t):
            if cha_s in s_to_t:
                if s_to_t[cha_s] != cha_t:
                    return False
            else:
                s_to_t[cha_s] = cha_t

            if cha_t in t_to_s:
                if t_to_s[cha_t] != cha_s:
                    return False
            else:
                t_to_s[cha_t] = cha_s

        return True

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        t_to_s = {}

        for c1, c2 in zip(s, t):
            if (c1 not in s_to_t) and (c2 not in t_to_s):
                s_to_t[c1] = c2
                t_to_s[c2] = c1

            elif s_to_t.get(c1) != c2 or t_to_s.get(c2) != c1:
                return False

        return True
