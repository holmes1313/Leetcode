"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""
import collections


class Solution(object):
    def countCharacters2(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        counts = collections.Counter(chars)
        ans = 0

        for word in words:
            word_count = collections.Counter(word)
            good = True
            for cha in word:
                if word_count[cha] > counts.get(cha, 0):
                    good = False
                    break
            if good:
                ans += len(word)

        return ans

