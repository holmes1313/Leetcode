"""
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
 

Constraints:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""
import collections
import heapq


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(barcodes)

        max_heap = []
        for val, freq in count.items():
            heapq.heappush(max_heap, (-freq, val))

        ans = []
        prev_val = None
        prev_count = 0
        while max_heap:
            count, val = heapq.heappop(max_heap)
            ans.append(val)
            count += 1

            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_val))

            prev_val = val
            prev_count = count

        return ans
