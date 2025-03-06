"""
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.

 

Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]
 

Constraints:

1 <= s.length <= 105
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Step 1: Reverse the entire array
        s.reverse()
        # Step 2: Reverse each word
        start = 0
        for i in range(len(s)+1):
            if i == len(s) or s[i] == " ":
                s[start:i] = s[start:i][::-1]
                start = i + 1
        #s[start:] = s[start:][::-1]
        return s
    
    def reverseWords(self, s):

        def reverse(low, high):
            while low < high:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1

        reverse(0, len(s) - 1)

        prev = 0
        for i in range(len(s)):
            if s[i] == " ":
                reverse(prev, i-1)
                prev = i + 1
        reverse(prev, len(s)-1)

        return s
