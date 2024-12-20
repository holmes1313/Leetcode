"""
Given a string s containing only digits, return the 
lexicographically smallest string
 that can be obtained after swapping adjacent digits in s with the same parity at most once.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

 

Example 1:

Input: s = "45320"

Output: "43520"

Explanation:

s[1] == '5' and s[2] == '3' both have the same parity, and swapping them results in the lexicographically smallest string.

Example 2:

Input: s = "001"

Output: "001"

Explanation:

There is no need to perform a swap because s is already the lexicographically smallest.
"""
class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        for i in range(len(s_list)-1):
            left = int(s_list[i])
            right = int(s_list[i+1])
            if left % 2 == right % 2 and left > right:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                break

        return "".join(s_list)