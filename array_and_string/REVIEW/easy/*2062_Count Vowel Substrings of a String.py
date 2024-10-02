"""
A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

 

Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
"""
class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        i = 0
        while i < len(word):
            if word[i] in vowels:
                j = i
                substring = set()
                while j < len(word) and word[j] in vowels:
                    substring.add(word[j])
                    if len(substring) == 5:
                        ans += 1
                    j += 1
            i += 1

        return ans
