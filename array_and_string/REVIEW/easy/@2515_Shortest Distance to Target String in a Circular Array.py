"""
You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.

 

Example 1:

Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.
"""
class Solution(object):
    def closetTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        target_indices = []
        for i, word in enumerate(words):
            if word == target:
                target_indices.append(i)

        if not target_indices:
            return -1

        min_distance = float('inf')
        for idx in target_indices:
            forward_distance = (idx - startIndex + n) % n
            backward_distance = (startIndex - idx + n) % n

            min_distance = min(min_distance, forward_distance, backward_distance)
        
        return min_distance

    def closetTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        if words[startIndex] == target:
            return 0
        
        n = len(words)
        startIndex %= n
        for i in range(1, n):
            left = (startIndex - i + n) % n
            right = (startIndex + i) % n
            if words[left] == target or words[right] == target:
                return i

        return -1
