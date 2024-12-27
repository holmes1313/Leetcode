"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

 

Example 1:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
Example 2:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
 
"""
class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # for a component to be complete, it must have the maximum possible edges, which is (k * (k - 1)) // 2 for k nodes.
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        completes = 0
        seen = set()

        def dfs(node):
            node_count = 0
            edge_count_directional = 0
            stack = [node]
            
            while stack:
                node = stack.pop()
                if node not in seen:
                    seen.add(node)
                    node_count += 1
                    edge_count_directional += len(graph[node])

                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            stack.append(neighbor)
            return node_count, edge_count_directional // 2       # Each edge is counted twice

        for node in range(n):
            if node not in seen:
                node_count, edge_count = dfs(node)
                if edge_count == node_count * (node_count - 1) // 2:
                    completes += 1

        return completes