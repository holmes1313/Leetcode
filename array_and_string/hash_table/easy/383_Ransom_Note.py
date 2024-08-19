"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = collections.Counter(magazine)
        for cha in ransomNote:
            if counter[cha] == 0:
                return False
            else:
                counter[cha] -= 1

        return True


class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count1 = collections.Counter(ransomNote)
        count2 = collections.Counter(magazine)

        for cha in count1:
            if count1[cha] > count2.get(cha, 0):
                return False

        return True
        