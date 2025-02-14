# https://www.1point3acres.com/bbs/thread-644592-1-1.html

"""

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        def backtrack(start, curr):
            if start == len(s):
                result.append(" ".join(curr))
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    curr.append(word)
                    backtrack(end, curr)
                    curr.pop()
        result = []
        backtrack(0, [])
        return result

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)

        memo = {}

        def backtrack(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            result = []
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in word_set:
                    strings = backtrack(end)
                    for part in strings:
                        if part:
                            result.append(word + " " + part)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return backtrack(0)
