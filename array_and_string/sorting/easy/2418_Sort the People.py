"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

"""
class Solution(object):
    def sortPeople2(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        mapping = {}
        for name, height in zip(names, heights):
            mapping[height] = name

        ans = []
        heights.sort(reverse=True)
        for height in heights:
            ans.append(mapping[height])

        return ans

    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype:
        """
        combined = list(zip(names, heights))
        combined.sort(key=lambda x: x[1], reverse=True)
        ans = [name for name, _ in combined]
        return ans
