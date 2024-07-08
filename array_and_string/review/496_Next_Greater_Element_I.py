"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""
class Solution(object):
    def nextGreaterElement2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        idx_mapping = {}
        for idx, num in enumerate(nums2):
            idx_mapping[num] = idx

        output = []
        for num in nums1:
            start = idx_mapping[num]
            find_next_greater = False
            for i in range(start, len(nums2)):
                if nums2[i] > num:
                    output.append(nums2[i])
                    find_next_greater = True
                    break
            if not find_next_greater:
                output.append(-1)

        return output

    def nextGreaterElement3(self, nums1, nums2):
        nums1_idx = {val: idx for idx, val in enumerate(nums1)}
        result = [-1 for _ in range(len(nums1))]

        for i in range(len(nums2)):
            if nums2[i] in nums1_idx:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        idx = nums1_idx[nums2[i]]
                        result[idx] = nums2[j]
                        break

        return result

    # Monotonic Stack
    # https://leetcode.com/problems/next-greater-element-i/editorial/
    def nextGreaterElement(self, nums1, nums2):
        nums1_idx = {val: idx for idx, val in enumerate(nums1)}
        result = [-1 for _ in range(len(nums1))]
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and stack[-1] < curr:
                val = stack.pop()
                idx = nums1_idx[val]
                result[idx] = curr
            if curr in nums1_idx:
                stack.append(curr)

        return result
