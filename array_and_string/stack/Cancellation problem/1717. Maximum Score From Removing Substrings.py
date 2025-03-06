"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

"""
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        if x > y:
            top_pair = "ab"
            top_score = x
            sec_pair = "ba"
            sec_score = y
        else:
            top_pair = "ba"
            top_score = y
            sec_pair = "ab"
            sec_score = x

        stack = []
        stack2 = []
        points = 0

        for cha in s:
            if cha == top_pair[1] and stack and stack[-1] == top_pair[0]:
                stack.pop()
                points += top_score
            else:
                stack.append(cha)

        for cha in stack:
            if cha == sec_pair[1] and stack2 and stack2[-1] == sec_pair[0]:
                stack2.pop()
                points += sec_score
            else:
                stack2.append(cha)

        return points