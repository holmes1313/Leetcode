"""
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

"""
class Solution(object):
    def checkString2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        first_b = -1
        last_a = -1
        p1 = 0
        p2 = len(s) - 1
        while p1 < len(s) or p2 >= 0:
            if first_b >= 0 and last_a >= 0:
                break

            if s[p1] == "b" and first_b < 0:
                first_b = p1

            if s[p2] == "a" and last_a < 0:
                last_a = p2
            
            p1 += 1
            p2 -= 1

        return first_b < 0 or last_a < 0 or first_b > last_a

    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        first_b = len(s)
        last_a = -1

        for i in range(len(s)):
            if s[i] == "a":
                last_a = max(i, last_a)
            if s[i] == "b":
                first_b = min(i, first_b)

        return first_b == len(s) or last_a == -1 or last_a < first_b
