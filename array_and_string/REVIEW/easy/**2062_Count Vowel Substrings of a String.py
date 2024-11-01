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
        count = 0
        for i in range(len(word)):
            j = i
            vowel_set = set()
            while j < len(word) and word[j] in vowels:
                vowel_set.add(word[j])
                if vowel_set == vowels:
                    count += 1
                j += 1
        return count

    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        count = 0
        n = len(word)
        for start in range(n):
            vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
            end = start
            while end < n and word[end] in vowels:
                vowels[word[end]] += 1
                if 0 not in vowels.values():
                    count += 1
                end += 1

        return count
