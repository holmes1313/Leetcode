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

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        mapping = {}
        output = []
        for item in items:
            if item[0] not in mapping:
                mapping[item[0]] = [item[1]]
            else:
                mapping[item[0]].append(item[1])

        for id, ss in mapping.items():
            ss.sort(reverse=True)
            if len(ss) > 5:
                ss = ss[:5]
            avg = sum(ss) / len(ss)
            avg_item = [id, avg]
            output.append(avg_item)

        return output
        

test = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
sorted(test, reverse=True)
highFive(test)


import collections
import heapq
def highFive_priorityQueue(items):
    """
    :type items: List[List[int]]
    :rtype: List[List[int]]
    """
    result = collections.defaultdict(list)
    
    for id, score in items:
        heapq.heappush(result[id], score)
        
        if len(result[id]) > 5:
            heapq.heappop(result[id])
    
    return [[id, sum(scores)/len(score)] for id, scores in sorted(result.items())]


a = [3, 1, 2]        
b = []
for i in a:
    heapq.heappush(b, i)
b
heapq.heappop(b)
