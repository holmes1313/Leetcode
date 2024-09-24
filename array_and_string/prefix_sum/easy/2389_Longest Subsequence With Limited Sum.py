"""
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
Example 2:

Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.
 



"""
from bisect import bisect_right
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        ans = []

        def bisect_right(array, num):
            left = 0
            right = len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] == num:
                    left = mid + 1
                elif array[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def bisect_right1(array, num):
            left = 0
            right = len(array)
            while left < right:
                mid = (left + right) // 2
                if array[mid] <= num:
                    left = mid + 1
                else:
                    right = mid - 1
            return left


        for query in queries:
            idx1 = bisect_right(nums, query)
            idx = bisect_right1(nums, query)
            ans.append(idx)

        return ans


    def answerQueries1(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        ans = []

        for query in queries:
            found = 0
            for idx, num in enumerate(nums):
                if query - num < 0:
                    ans.append(idx)
                    found = 1
                    break

            if not found:
                ans.append(len(nums))
                

        return ans
                

        