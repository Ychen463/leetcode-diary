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

# # ================== Approach 2: Breadth First Search ==================
# from collections import deque
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         def bfs(start):
#             queue = deque([start])
#             while queue:
#                 node = queue.popleft()
#                 for neighbor, is_connected in enumerate(isConnected[node]):
#                     if neighbor not in visited and is_connected:
#                         queue.append(neighbor)
#                         visited.add(neighbor)
#         visited = set()
#         count = 0
#         for i in range(len(isConnected)):
#             if i not in visited:
#                 visited.add(i)
#                 bfs(i)
#                 count +=1
#         return count

# ================== Approach 2: Breadth First Search ==================
class Solution:
    # Union-Find
    # 是一种用于处理不相交集合（disjoint set）数据结构的工具，特别适用于动态连通性问题。
    # 思路
        # 1. 将每个城市视为一个节点，初始时每个城市自成一个集合。
        # 2. 遍历邻接矩阵 isConnected，如果 isConnected[i][j] == 1 且 i != j，
        #       则将城市 i 和城市 j 合并到同一个集合中。
        # 3. 最后，统计集合的数量，即为省份的数量。
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        province_count = len(set(uf.find(i) for i in range(n)))
        return province_count
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1