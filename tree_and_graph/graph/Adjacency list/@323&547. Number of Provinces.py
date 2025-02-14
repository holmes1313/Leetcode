"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""
import collections


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)

        n = len(isConnected)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)
                    graph[j+1].append(i+1)
        
        seen = set()
        count = 0

        def dfs(city):
            seen.add(city)
            for neighbor in graph.get(city, []):
                if neighbor not in seen:
                    dfs(neighbor)

        for city in range(1, n+1):
            if city not in seen:
                count += 1
                #dfs(city)
                stack = [city]
                while stack:
                    node = stack.pop()
                    seen.add(node)
                    for neighbor in graph.get(node, []):
                        if neighbor not in seen:
                            stack.append(neighbor)
                        
        return count
