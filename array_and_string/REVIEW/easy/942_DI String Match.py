"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
"""

# Keep track of the smallest and largest element we haven't placed. 
# If we see an 'I', place the small element; otherwise place the large element.

class Solution(object):
    def diStringMatch2(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        nums = [i for i in range(len(s)+1)]
        left = 0
        right = len(nums) - 1
        result = []
        for cha in s:
            if cha == "I":
                result.append(nums[left])
                left += 1
            elif cha == "D":
                result.append(nums[right])
                right -= 1

        result.append(nums[left])
        return result


    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        left = 0
        right = len(s)
        ans = []
        for cha in s:
            if cha == "I":
                ans.append(left)
                left += 1
            elif cha == "D":
                ans.append(right)
                right -= 1

        ans.append(left)
        return ans
