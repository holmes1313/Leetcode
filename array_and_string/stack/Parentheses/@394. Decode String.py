"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for cha in s:
            if cha == "]":
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                stack.pop()
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                stack.append(curr_str * int(curr_num))
            else:
                stack.append(cha)

        return "".join(stack)

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr_num = 0
        curr_str = ""
        for cha in s:
            if cha.isdigit():
                curr_num = curr_num * 10 + int(cha)
            elif cha == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif cha == "]":
                prev_str, k = stack.pop()
                curr_str = prev_str + k*curr_str
            else:
                curr_str += cha

        return curr_str
