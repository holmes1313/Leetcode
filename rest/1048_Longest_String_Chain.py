# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:59:44 2019

@author: z.chen7
"""
# 1048. Longest String Chain
"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one 
letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, 
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 
Note:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""

# sub combinations
w = 'abcd'
[w[:i] + w[i+1: ] for i in range(len(w))]


"""
Explanation
Sort the words by word's length. (also can apply bucket sort)
For each word, loop on all possible previous word with 1 letter missing.
If we have seen this previous word, add 1 to the previous longest chain for the current word.
Finally return the longest word chain.
"""
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dp = {}
        for word in sorted(words, key=len):
            predecessors = [word[:i] + word[i+1:] for i in range(len(word))]
            dp[word] = max([dp.get(p, 0) for p in predecessors]) + 1
            
        return max(dp.values())