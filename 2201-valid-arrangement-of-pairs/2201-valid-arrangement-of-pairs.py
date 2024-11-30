from collections import deque, defaultdict
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
        # Step 1. 
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for u, v in pairs:
            graph[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1
        
        # Step 2. find start
        start = None
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start = node
                break
        if start == None:
            start = pairs[0][0]
        
        # Step 3: Hierholzer 算法，深度优先搜索构建路径
        path = []
        stack = [start]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].popleft())
            path.append(stack.pop())
        # Step 4: 反转路径，构造结果
        path.reverse()
        result = [[path[i], path[i+1]] for i in range(len(path) - 1)]

        return result 

