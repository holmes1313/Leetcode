"""
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar.

 

Example 1:

Input: words = ["aba","aabb","abcd","bac","aabc"]
Output: 2
Explanation: There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 
"""
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        mapping = collections.defaultdict(int)
        for word in words:
            key = tuple(sorted(set(word)))
            mapping[key] += 1

        ans = 0
        for val in mapping.values():
            # add pairs using the unique combination formula
            # 1+ 2 + ... + (val-1)
            # val * (val - 1) // 2
            count = val*(val-1)//2
            ans += count

        return ans
        

class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_sets = [set(word) for word in words]
        ans = 0
        for i in range(len(word_sets) - 1):
            for j in range(i+1, len(word_sets)):
                if word_sets[i] == word_sets[j]:
                    ans += 1

        return ans