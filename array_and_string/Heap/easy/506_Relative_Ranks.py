"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.



Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
"""
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        ordered_score = sorted(score, reverse=True)
        order_map = {}
        for i, val in enumerate(ordered_score):
            if i == 0:
                rank = "Gold Medal"
            elif i == 1:
                rank = "Silver Medal"
            elif i == 2:
                rank = "Bronze Medal"
            else:
                rank = str(i+1)

            order_map[val] = rank

        result = []
        for val in score:
            result.append(order_map[val])

        return result

    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # max heap
        heap = []
        for i, val in enumerate(score):
            heapq.heappush(heap, (-val, i))

        ans = [0] * len(score)
        rank = 1
        while heap:
            origin_index = heapq.heappop(heap)[1]
            if rank == 1:
                ans[origin_index] = "Gold Medal"
            elif rank == 2:
                ans[origin_index] = "Silver Medal"
            elif rank == 3:
                ans[origin_index] = "Bronze Medal"
            else:
                ans[origin_index] = str(rank)
            rank += 1

        return ans