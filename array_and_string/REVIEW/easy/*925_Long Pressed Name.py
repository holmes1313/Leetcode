"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        p1 = p2 = 0

        while p1 < len(name) and p2 < len(typed):
            if name[p1] != typed[p2]:
                return False

            cha = name[p1]
            count1 = count2 = 0
            while p1 < len(name) and name[p1] == cha:
                count1 += 1
                p1 += 1
            while p2 < len(typed) and typed[p2] == cha:
                count2 += 1
                p2 += 1
            if count1 > count2:
                return False

        return p1 == len(name) and p2 == len(typed)