# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:08:07 2019

@author: z.chen7
"""
# 127. Word Ladder

"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = collections.deque()
        queue.appendleft((beginWord, 1))
        visited = set()
        letters = string.ascii_lowercase
        wordList = set(wordList)
        
        while queue:
            word, length = queue.pop()
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for j in letters:
                    if j != word[i]:
                        newWord = word[:i] + j + word[i+1:]
                        if newWord in wordList and newWord not in visited:
                            queue.appendleft((newWord, length + 1))
                            visited.add(newWord)
        return 0
        