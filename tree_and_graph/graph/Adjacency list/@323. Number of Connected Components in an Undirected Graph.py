"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 


"""
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        components = 0
        stack = []

        for node in range(n):
            if node not in seen:
                components += 1
                stack.append(node)

                while stack:
                    n = stack.pop()
                    if n not in seen:
                        seen.add(n)
                        for neighbor in graph[n]:
                            stack.append(neighbor)

        return components


        