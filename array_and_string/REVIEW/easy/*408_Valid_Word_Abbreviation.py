"""
lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.



Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
"""
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0  # Pointers for word and abbr
        n, m = len(word), len(abbr)

        while i < n and j < m:
            if abbr[j].isdigit():
                # If the current character is a digit, read the full number
                if abbr[j] == '0':
                    return False  # Leading zero is not allowed
                num = 0
                while j < m and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])  # Build the number
                    j += 1
                i += num  # Skip 'num' characters in 'word'
            else:
                # If it's a letter, match it with the 'word'
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False  # Mismatch
        
        # Check if we have processed all characters in both strings
        return i == n and j == m