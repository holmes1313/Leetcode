"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

"""
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        p1 = 0
        p2 = len(s) - 1
        s_list = list(s)
        while p1 < p2:
            if not s_list[p1].isalpha():
                p1 += 1
                continue

            if not s_list[p2].isalpha():
                p2 -= 1
                continue

            s_list[p1], s_list[p2] = s_list[p2], s_list[p1]
            p1 += 1
            p2 -= 1

        return "".join(s_list)

