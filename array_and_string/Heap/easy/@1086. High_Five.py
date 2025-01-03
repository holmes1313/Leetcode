# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:55:04 2019

@author: z.chen7
"""

# 1086. High Five
"""
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 

Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
"""
import collections
import heapq


class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        score_dict = collections.defaultdict(list)

        for sid, score in items:
            heapq.heappush(score_dict[sid], score)
            if len(score_dict[sid]) > 5:
                heapq.heappop(score_dict[sid])

        result = []
        for sid in sorted(score_dict.keys()):
            high_five = score_dict[sid]
            average = sum(high_five) // 5
            result.append([sid, average])

        return result
        

    