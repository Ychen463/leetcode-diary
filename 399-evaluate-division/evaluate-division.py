from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b),value in zip(equations,values):
            graph[a][b]=value
            graph[b][a]=1/value
        print(graph)
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1
            queue = deque([(start, 1.0)])
            visited = set()
            while queue:
                current, product = queue.popleft()
                if current == end:
                    return product
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, product * value))
            return -1.0
        
        # 
        result = []
        for C, D in queries:
            result.append(bfs(C, D))
        return result

