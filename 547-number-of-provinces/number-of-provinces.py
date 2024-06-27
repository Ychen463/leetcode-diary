# # ================== Approach 1: Depth First Search =================
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         def dfs(node):
#             # 只访问直接相连且未访问过的节点: [1,1,0]
#             for neighbor, is_connected in enumerate(isConnected[node]):
#                 if neighbor not in visited and is_connected:
#                     visited.add(neighbor)
#                     dfs(neighbor)
#         visited = set()
#         count = 0
#         for i in range(len(isConnected)):
#             if i not in visited:
#                 visited.add(i)
#                 dfs(i)
#                 count +=1
#         return count

# ================== Approach 2: Breadth First Search ==================
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(node):
            queue = deque([node])
            while queue:
                node = queue.popleft()
                for neighbor, is_connected in enumerate(isConnected[node]):
                    if neighbor not in visited and is_connected:
                        queue.append(neighbor)
                        visited.add(neighbor)
        visited = set()
        count = 0
        for i in range(len(isConnected)):
            if i not in visited:
                count+=1
                bfs(i)
                visited.add(i)
        return count