"""
You are given a string array words and a binary array groups both of length n, where words[i] is associated with groups[i].

Your task is to select the longest alternating 
subsequence
 from words. A subsequence of words is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array groups differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the groups array.

Formally, you need to find the longest subsequence of an array of indices [0, 1, ..., n - 1] denoted as [i0, i1, ..., ik-1], such that groups[ij] != groups[ij+1] for each 0 <= j < k - 1 and then find the words corresponding to these indices.

Return the selected subsequence. If there are multiple answers, return any of them.

Note: The elements in words are distinct.

 

Example 1:

Input: words = ["e","a","b"], groups = [0,0,1]

Output: ["e","b"]

Explanation: A subsequence that can be selected is ["e","b"] because groups[0] != groups[2]. Another subsequence that can be selected is ["a","b"] because groups[1] != groups[2]. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is 2.
"""
class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        if not words:
            return []
        
        found_one = False
        found_zero = False
        ans = [words[0]]
        if groups[0] == 0:
            found_zero = True
        else:
            found_one = True

        for i in range(1, len(words)):
            if groups[i] == 0 and found_one:
                ans.append(words[i])
                found_zero = True
                found_one = False
            elif groups[i] == 1 and found_zero:
                ans.append(words[i])
                found_one = True
                found_zero = False

        return ans

    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        ans = []

        if words:
            ans.append(words[0])

        for i in range(1, len(words)):
            if groups[i] != groups[i-1]:
                ans.append(words[i])

        return ans

        