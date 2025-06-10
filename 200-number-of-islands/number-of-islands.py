class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        Directions = [[1,0],[0,1],[0,-1],[-1,0]]
        islands = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                x,y = q.popleft()
                for dx,dy in Directions:
                    nx,ny = x+dx,y+dy
                    if nx in range(ROW) and ny in range(COL) and grid[nx][ny] == "1" and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx,ny)) 

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands +=1
        return islands 
        