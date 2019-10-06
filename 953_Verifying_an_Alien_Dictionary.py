# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:30:39 2019

@author: z.chen7
"""

# 953. Verifying an Alien Dictionary
"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters."""


"""
Approach 1: Check Adjacent Words
Intuition

The words are sorted lexicographically if and only if adjacent words are. This is because order is transitive: a <= b and b <= c implies a <= c.

Algorithm

Let's check whether all adjacent words a and b have a <= b.

To check whether a <= b for two adjacent words a and b, we can find their first difference. For example, "applying" and "apples" have a first difference of y vs e. After, we compare these characters to the index in order.

Care must be taken to deal with the blank character effectively. If for example, we are comparing "app" to "apply", this is a first difference of (null) vs "l"
"""

# for else combination
"""
"find some item in the iterable, else if none was found do ...". As in:

found_obj = None
for obj in objects:
    if obj.key == search_key:
        found_obj = obj
        break
else:
    print('No object found.')
"""
# enumerate
# The words are sorted lexicographically if and only if adjacent words are

def isAlienSorted(words, order):
    order_index = {l: i for i, l in enumerate(order)}
    
    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]
        
        # find the first difference word1[j] != word2[j]
        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if order_index[word1[j]] > order_index[word2[j]]:
                    return False
                break
            
        else:
            # if we didn't find a first difference
            # the words are like "app" and "apple"
            if len(word1) > len(word2):
                return False
            
    return True


isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
