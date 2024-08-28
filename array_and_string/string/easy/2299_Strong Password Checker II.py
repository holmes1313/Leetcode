"""
A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.

 

Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.

"""

class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        if len(password) < 8:
            return False
        
        lower_check = False
        upper_check = False
        digit_check = False
        special_check = False
        adjacent_check = True
        specials = set("!@#$%^&*()-+")
        for i in range(len(password)):
            if password[i].islower():
                lower_check = True
            if password[i].isupper():
                upper_check = True
            if password[i].isnumeric():
                digit_check = True
            if password[i] in specials:
                special_check = True

            if i < len(password) - 1 and password[i] == password[i+1]:
                adjacent_check = False

        return lower_check and upper_check and digit_check and special_check and adjacent_check
        
                

        