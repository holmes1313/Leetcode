"""
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
 
 """

 class Solution(object):
    def maxLengthBetweenEqualCharacters2(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}
        largest = -1
        for idx, cha in enumerate(s):
            if cha not in mapping:
                mapping[cha] = [idx]
            else:
                mapping[cha].append(idx)
        
        for values in mapping.values():
            largest = max(largest, values[-1] - values[0] - 1)

        return largest

    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        first_index = {}
        ans = -1

        for idx, cha in enumerate(s):
            if cha in first_index:
                ans = max(ans, idx - first_index[cha] - 1)
            else:
                first_index[cha] = idx

        return ans