class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        #
        degree = [0]*n
        for road in roads:
            degree[road[0]] +=1
            degree[road[1]] +=1
        # 
        nodes = [(i, degree[i]) for i in range(len(degree))]   
        nodes.sort(key = lambda x:x[1], reverse = True)
        print(nodes)
        print(degree)

        # 
        importance = [0] * n
        for i in range(len(degree)):
            importance[nodes[i][0]] = n - i
        print(importance)
        # 计算总重要性值
        total_importance = 0
        for road in roads:
            total_importance += importance[road[0]] + importance[road[1]]
        
        return total_importance

