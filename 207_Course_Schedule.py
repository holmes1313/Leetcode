# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 10:26:03 2019

@author: z.chen7
"""
# 207. Course Schedule
"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to 
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # indegree
        parents = {course: set() for course in range(numCourses)}
        children = collections.defaultdict(set)
        # Empty list that will contain the sorted elements
        buildOrder = []
        
        for c, prereq in prerequisites:
            parents[c].add(prereq)
            children[prereq].add(c)
        
        queue = collections.deque()
        
        for p in parents:
            if len(parents[p]) == 0:
                queue.appendleft(p)
                
        while queue:
            """
            while queue is non-empty do
                remove parent from parents
                add parent to tail of buildOrder
                for each child with with this parent
                    remove this parent from the child
                    if child has no other incoming edges (parent) then
                        insert child into queue
            """
            parent = queue.popleft()
            buildOrder.append(parent)
            del parents[parent]

            for child in children[parent]:
                parents[child].remove(parent)
                if not parents[child]:
                    queue.appendleft(child)
                
        return not parents
                
        



