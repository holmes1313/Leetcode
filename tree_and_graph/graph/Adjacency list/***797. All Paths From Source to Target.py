"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # Involves backtracking because you must explore all paths, 
        # and you need to retract your steps (backtrack) when you hit a dead-end or a node that doesn't lead to the destination.
        def backtrack(node, curr):
            if node == target:
                result.append(curr[:])
                return

            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    curr.append(neighbor)
                    backtrack(neighbor, curr)
                    curr.pop()
                    seen.remove(neighbor)

        target = len(graph) - 1
        # In a DAG, there are no cycles, so you don’t need to track visited nodes.
        seen = set()
        result = []
        backtrack(0, [0])
        return result

