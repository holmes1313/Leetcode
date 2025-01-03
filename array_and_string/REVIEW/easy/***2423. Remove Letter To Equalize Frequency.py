"""
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot choose to do nothing.
 

Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.

"""
import collections


class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        counts = collections.Counter(word)

        freq_counts = collections.Counter(counts.values())

        if len(freq_counts) == 2:
            if freq_counts.get(1) == 1:
                return True

            (f1, c1), (f2, c2) = freq_counts.items()
            if abs(f1 - f2) == 1 and freq_counts[max(f1, f2)] == 1:
                return True
        
        if len(freq_counts) == 1:
            return 1 in freq_counts or 1 in freq_counts.values()
        
        return False

    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        counts = collections.Counter(word)

        for cha in counts.keys():
            counts[cha] -= 1

            if counts[cha] == 0:
                del counts[cha]

            if len(set(counts.values())) == 1:
                return True

            counts[cha] += 1

        return False
            
