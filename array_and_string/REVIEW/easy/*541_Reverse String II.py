"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        slist = list(s)
        for i in range(0, len(slist), 2* k):
            slist[i: i+k] = slist[i:i+k][::-1]
        return "".join(slist)

    def reverseStr1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        slist = list(s)
        reverse = True
        for i in range(0, len(slist), k):
            if reverse:
                slist[i:i+k] = slist[i:i+k][::-1]
                reverse = False
            else:
                reverse = True
        return "".join(slist)