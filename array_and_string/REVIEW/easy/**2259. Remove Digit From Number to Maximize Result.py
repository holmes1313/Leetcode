"""
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.

 

Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
Example 2:

Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".
"""
class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        ans = float('-inf')
        for idx, cha in enumerate(number):
            if cha == digit:
                ans = max(ans, int(number[:idx] + number[idx+1:]))

        return str(ans)

    def removeDigit(self, number, digit):
        for i in  range(len(number)-1):
            if number[i] == digit and number[i] < number[i+1]:
                return number[:i] + number[i+1:]

        # else, remove the last occurence of the digit
        last_idx = number.rfind(digit)
        return number[:last_idx] + number[last_idx+1:]
