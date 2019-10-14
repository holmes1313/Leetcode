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


def highFive(items):
    """
    :type items: List[List[int]]
    :rtype: List[List[int]]
    """
    result = {}
    result_list = []
    for i in items:
        if i[0] not in result:
            result[i[0]] = [i]
        else:
            result[i[0]].append(i)
            
    
    for i, v in result.items():
        v.sort(reverse=True)
        if len(v) > 5:
            v = v[:5]
        scores = [s[1] for s in v] 
        average = sum(scores) / len(scores)
        result_list.append([i, average])

    return result_list
        

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
