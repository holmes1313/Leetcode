"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        p_count = collections.Counter(p)
        window_count = collections.Counter()
        ans = []

        for i in range(len(s)):
            window_count[s[i]] += 1

            if i >= len(p):
                start_cha = s[i-len(p)]
                window_count[start_cha] -= 1
                if window_count[start_cha] == 0:
                    del window_count[start_cha]

            if window_count == p_count:
                ans.append(i-len(p)+1)

        return ans