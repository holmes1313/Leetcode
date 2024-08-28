"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0

"""
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = collections.Counter(text)
        ans = 0
        while True:
            finish = 1
            for cha in "balloon":
                if counter[cha] == 0:
                    finish = 0
                    break
                counter[cha] -= 1
            if finish:
                ans += 1
            else:
                break

        return ans