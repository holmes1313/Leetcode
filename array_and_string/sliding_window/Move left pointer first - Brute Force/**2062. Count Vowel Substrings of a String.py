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
        count = 0
        vowels = set('aeiou')
        n = len(word)
        for start in range(n):
            found_vowels = set()
            for end in range(start, n):
                if word[end] in vowels:
                    found_vowels.add(word[end])
                else:
                    break
                if len(found_vowels) == len(vowels):
                    count += 1
        return count

    def countVowelSubstrings(self, word):
        vowels = set("aeiou")
        left = 0
        n = len(word)
        count = 0
        for left in range(len(word)):
            if word[left] not in vowels:
                continue
            curr_vowels = set()
            right = left
            while right < n and word[right] in vowels:
                curr_vowels.add(word[right])
                if len(curr_vowels) == len(vowels):
                    count += 1
                right += 1
    
        return count
