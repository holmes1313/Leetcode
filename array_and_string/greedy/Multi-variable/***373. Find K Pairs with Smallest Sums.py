"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 105
-109 <= nums1[i], nums2[i] <= 109
nums1 and nums2 both are sorted in non-decreasing order.
1 <= k <= 104
k <= nums1.length * nums2.length
"""
import heapq


class Solution(object):
    def kSmallestPairs2(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = []

        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(min_heap, (n1+n2, n1, n2))
                

        result = []
        for _ in range(k):
            _, n1, n2 = heapq.heappop(min_heap)
            result.append([n1, n2])

        return result

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i]+nums2[0], i, 0))

        result = []

        while k > 0:
            _, x, y = heapq.heappop(min_heap)
            result.append([nums1[x], nums2[y]])
            k -= 1
            if y + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[x]+nums2[y+1], x, y+1))

        return result

