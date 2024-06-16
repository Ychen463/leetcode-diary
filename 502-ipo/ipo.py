class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 将项目按启动资金进行排序
        projects = sorted(zip(capital ,profits ), key = lambda x: x[0])

        min_capital_heap = []
        max_profit_heap = []
        
        i = 0
        n = len(projects)
    
        for _ in range(k):
            # 将当前可以启动的项目放入大顶堆
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_profit_heap, -projects[i][1])  # 利润取负数，便于使用大顶堆
                i += 1
            
            # 如果大顶堆为空，表示没有可以启动的项目了
            if not max_profit_heap:
                break
            
            # 选择利润最大的项目
            w += -heapq.heappop(max_profit_heap)
        
        return w