"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]


Example 2:

Input: n = 1
Output: [[1]]
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.allPossibleBTS(1, n, memo)

    def allPossibleBTS(self, start, end, memo):
        if start > end:
            return [None]

        if start == end:
            return [TreeNode(start)]

        if (start, end) in memo:
            return memo[(start, end)]

        res = []
        for i in range(start, end + 1):
            leftSubTrees = self.allPossibleBTS(start, i - 1, memo)
            rightSubTrees = self.allPossibleBTS(i + 1, end, memo)
            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i, left, right)
                    res.append(root)

        memo[(start, end)] = res
        return res

