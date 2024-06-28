# =================== Approach 1: Depth First Search ===================
# from collections import defaultdict
# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         # 构造紧邻表
#         graph = defaultdict(list)
#         for a, b  in connections:
#             graph[a].append((b, True))
#             graph[b].append((a, False))
#         def dfs(node, parent):
#             nonlocal changes
#             for neighbor, to_reverse in graph[node]:
#                 if neighbor==parent:
#                     continue
#                 if to_reverse:
#                     changes+=1
#                 dfs(neighbor, node)
#         
#         # 记录需要翻转的道路数
#         changes = 0
#         dfs(0, -1)
#         return changes
# =================== Approach 2: Breadth First Search ===================
from collections import deque, defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 构造紧邻表
        graph = defaultdict(list)
        for a, b  in connections:
            graph[a].append((b, True))
            graph[b].append((a, False))
        queue = deque([0])
        changes = 0
        visited = set([0])
        
        while queue:
            node = queue.popleft()
            for neighbor, is_reverse in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if is_reverse:
                        changes +=1
                    queue.append(neighbor)        
        return changes