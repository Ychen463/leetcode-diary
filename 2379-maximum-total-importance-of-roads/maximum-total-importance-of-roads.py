class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        nodes = [(i, degree[i]) for i in range(n)]
        nodes.sort(key = lambda x: x[1], reverse = True)
        
        importances = [0] * n
        for i in range(len(nodes)):
            importances[nodes[i][0]] = n - i
        total_importance = 0
        for road in roads:
            total_importance += importances[road[0]] + importances[road[1]]
        return total_importance


