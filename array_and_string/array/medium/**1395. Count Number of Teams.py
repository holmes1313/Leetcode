"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4

"""
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        teams = 0
        n = len(rating)
        # Iterate through each soldier as the middle soldier of the team
        for j in range(1, n-1):
            greater_before = 0
            less_before = 0

            greater_after = 0
            less_after = 0

            # Count how many ratings are smaller/larger than rating[j] on the left
            for i in range(j):
                if rating[i] > rating[j]:
                    greater_before += 1
                else:
                    less_before += 1
            # Count how many ratings are smaller/larger than rating[j] on the right
            for k in range(j+1, len(rating)):
                if rating[k] > rating[j]:
                    greater_after += 1
                else:
                    less_after += 1
            # # Calculate valid teams with rating[j] as the middle soldier
            teams += less_before * greater_after + greater_before * less_after

        return teams