class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for dx, dy in directions:
                dfs(i+dx, j+dy)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1

                    queue = collections.deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
                            continue
                        grid[x][y] = "0"
                        for dx, dy in directions:
                            queue.append((x+dx, y+dy))
                    #dfs(i, j)
        return count
