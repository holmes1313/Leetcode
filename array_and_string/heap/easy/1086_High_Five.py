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
    def highFive2(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        mapping = collections.defaultdict(list)
        output = []
        for item in items:
            mapping[item[0]].append(item[1])

        for id, ss in mapping.items():
            ss.sort(reverse=True)
            if len(ss) > 5:
                ss = ss[:5]
            avg = sum(ss) / len(ss)
            avg_item = [id, avg]
            output.append(avg_item)

        return output

        

    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        mapping = collections.defaultdict(partial(MinHeap, size=5))

        for item in items:
            mapping[item[0]].add(item[1])
        
        ordered_ids = sorted(mapping.keys())
        result = []
        for stu_id in ordered_ids:
            avg = mapping[stu_id].calc_avg()
            result.append([stu_id, avg])

        return result
        
class MinHeap():
    def __init__(self, size):
        self.size = size
        self.queue = []

    def add(self, score):
        heappush(self.queue, score)
        if len(self.queue) > self.size:
            heappop(self.queue)

    def calc_avg(self):
        return sum(self.queue) / len(self.queue)

    