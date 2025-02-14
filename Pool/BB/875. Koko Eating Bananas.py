class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canFinish(k):
            hours = 0
            for pile in piles:
                hours += (pile // k)
                if pile % k != 0:
                    hours += 1
                # hours += (pile + k - 1) // k
            return hours <= h

        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            if not canFinish(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left
