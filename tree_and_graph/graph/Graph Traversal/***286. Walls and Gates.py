"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]

"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        # BFS is particularly suitable here 
        # because it explores all rooms at the present depth level before moving on to rooms at the next depth level
        # ensuring that the shortest distance is found first.

        if not rooms:
            return 

        rows = len(rooms)
        cols = len(rooms[0])
        queue = collections.deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))


        while queue:
            i, j = queue.popleft()
            for x, y in directions:
                i_new = i + x
                j_new = j + y

                if 0 <= i_new < rows and 0 <= j_new < cols and rooms[i_new][j_new] == 2147483647:
                    rooms[i_new][j_new] = rooms[i][j] + 1
                    queue.append((i_new, j_new))

        return rooms
