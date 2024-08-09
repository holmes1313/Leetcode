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

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        p1 = 0
        p2 = 0
        while p1 < len(word) and p2 < len(abbr):
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1

            elif abbr[p2] == "0":
                return False

            elif abbr[p2].isnumeric():
                num = ""
                while p2 < len(abbr) and abbr[p2].isnumeric():
                    num += abbr[p2]
                    p2 += 1
                p1 += int(num)

            else:
                return False

        return p1 == len(word) and p2 == len(abbr)
