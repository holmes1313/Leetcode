"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False

            if visited[course] == 2:
                return True

            visited[course] = 1

            for neighbor in graph.get(course, []):
                if not dfs(neighbor):
                    return False

            visited[course] = 2
            return True


        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return False

        return True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        """
        Steps for Kahn's Algorithm (BFS-based approach):
        1.Build an adjacency list to represent the graph of courses and their prerequisites.
        2.Calculate the in-degree for each course. The in-degree represents how many prerequisites each course has (i.e., how many edges point to it).
        3.Use a queue to perform a topological sort:
        (a) Start with all courses that have an in-degree of 0 (i.e., no prerequisites).
        (b) For each course processed, reduce the in-degree of its dependent courses. If a dependent course’s in-degree becomes 0, add it to the queue.
        (c) Keep tracking of the courses as you process them.
        """
        graph = collections.defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        while queue:
            course = queue.popleft()
            count += 1

            for neighbor in graph.get(course, []):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses 