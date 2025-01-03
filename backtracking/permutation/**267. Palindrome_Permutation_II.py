"""
Given a string s, return all the palindromic permutations (without duplicates) of it.

You may return the answer in any order. If s has no palindromic permutation, return an empty list.

Example 1:
Input: s = "aabb"
Output: ["abba","baab"]

Example 2:
Input: s = "abc"
Output: []
"""
import collections


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtrack(path, counter):
            if len(path) == len(s) // 2:
                halves.append("".join(path[:]))
                return

            for cha in counter:
                if counter[cha] > 0:
                    path.append(cha)
                    counter[cha] -= 1
                    backtrack(path, counter)
                    counter[cha] += 1
                    path.pop()

        counter = collections.Counter(s)

        # Check Palindrome Feasibility
        odd_count = sum(1 for count in counter.values() if count % 2 == 1)
        if odd_count > 1:
            return []

        # Prepare a backtracking function that constructs half of the palindrome
        half_len = len(s) // 2
        mid_cha = ""
        half_count = {}
        for cha, count in counter.items():
            if count % 2 == 1:
                mid_cha = cha
            half_count[cha] = count // 2

        halves = []
        backtrack([], half_count)

        # Generate Full Palindromes
        result = [half + mid_cha + half[::-1] for half in halves]
        return result
