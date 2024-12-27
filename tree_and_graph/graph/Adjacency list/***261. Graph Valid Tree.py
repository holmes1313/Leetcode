"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        # Use an iterative DFS to check connectivity and detect cycles
        stack = [(0, -1)]   # (current_node, parent_node)

        while stack:
            node, parent = stack.pop()

            if node in visited:
                return False # Cycle detected
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != parent:
                    stack.append((neighbor, node))


        return len(visited) == n
        