from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, columns = len(maze), len(maze[0])
        # BFS 队列，储存位置和steps
        queue = deque([(entrance[0], entrance[1], 0)])
        # 记录已访问
        visited = set()
        visited.add((entrance[0],entrance[1]))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 开始遍历
        while queue:
            r, c, steps = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c+ dc
                # 检查知否在maze里面，且可以走
                if 0 <= nr < rows and 0 <= nc < columns and maze[nr][nc] == '.':
                    # 检查是否为出口
                    if (nr == 0 or nr == rows-1 or nc == 0 or nc == columns -1) and ([nr,nc] != entrance):
                        return steps + 1
                    # 如果不是出口，加入到visited
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc,steps+1))
        return -1