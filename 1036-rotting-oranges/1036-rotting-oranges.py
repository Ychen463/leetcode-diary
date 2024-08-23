from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0)) # 第0分钟的时候已经是rotten的了
                if grid[r][c] ==1:
                    fresh_oranges+=1
        # 如果没有新鲜橙子，直接返回 0
        if fresh_oranges == 0:
            return 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        mins = 0
        while queue:
            r, c, mins = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (0<=nr < rows and 0<=nc<cols and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append((nr,nc,mins+1))
        return -1 if fresh_oranges > 0 else mins

