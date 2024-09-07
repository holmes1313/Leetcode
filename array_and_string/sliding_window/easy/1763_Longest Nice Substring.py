"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

"""

    lower_set = set()
            upper_set = set()
            for char in sub:
                if char.islower():
                    lower_set.add(char)
                elif char.isupper():
                    upper_set.add(char)
            
            for char in lower_set:
                if char.upper() not in upper_set:
                    return False
            for char in upper_set:
                if char.lower() not in lower_set:
                    return False
            return True
        
        n = len(s)
        max_length = 0
        longest_substr = ""
        
        # Check all possible substrings
        for start in range(n):
            for end in range(start + 1, n + 1):
                substr = s[start:end]
                if is_nice(substr):
                    if len(substr) > max_length:
                        max_length = len(substr)
                        longest_substr = substr
        
        return longest_substr