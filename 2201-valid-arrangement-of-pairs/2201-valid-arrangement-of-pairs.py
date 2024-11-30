
# # ================== Approach 2: Hierholzer's Algorithm (Iterative) ================== 
# from collections import defaultdict, deque

# class Solution:
# def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
#     # Step 1: 构建邻接表和统计入度、出度
#     graph = defaultdict(deque)  # 使用 deque 确保顺序
#     in_degree = defaultdict(int)
#     out_degree = defaultdict(int)
    
#     for u, v in pairs:
#         graph[u].append(v)
#         out_degree[u] += 1
#         in_degree[v] += 1

#     # Step 2: 找到欧拉路径的起点
#     start = None
#     for node in graph:
#         if out_degree[node] > in_degree[node]:  # 出度比入度多的点是起点
#             start = node
#             break
#     if start is None:
#         start = pairs[0][0]  # 没有特殊起点时，任意选择一个点

#     # Step 3: Hierholzer 算法，深度优先搜索构建路径
#     path = []
#     stack = [start]

#     while stack:
#         while graph[stack[-1]]:
#             stack.append(graph[stack[-1]].popleft())
#         path.append(stack.pop())

#     # Step 4: 反转路径，构造结果
#     path.reverse()
#     result = [[path[i], path[i+1]] for i in range(len(path) - 1)]
#     return result

# ================== Approach 1: Eulerian Path (Recursive) ================== 
from collections import defaultdict, deque
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for u,v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1

        start = None
        for node in graph:
            if in_degree[node] < out_degree[node]:
                start = node
                break
        if start == None:
            start = pairs[0][0]

        # Step 3: 递归 DFS 构建路径
        path = []
        
        def dfs(node):
            while graph[node]:
                next_node = graph[node].popleft()  # 取出一个出边
                dfs(next_node)  # 递归访问下一个节点
            path.append(node)  # 当前节点回溯时加入路径
        
        dfs(start)

        # Step 4
        path.reverse()
        result = [[path[i], path[i+1]] for i in range(len(path) - 1)]
        return result


