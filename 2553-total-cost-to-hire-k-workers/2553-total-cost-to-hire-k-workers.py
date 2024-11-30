import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # 两个指针分别指向候选范围的开头和结尾
        left = 0
        right = len(costs) - 1
        
        # 两个最小堆
        left_heap = []
        right_heap = []

        # 初始化前 candidates 和后 candidates 范围的堆
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1
        total_cost = 0

        # 贪心选择 k 次
        for _ in range(k):
            if left_heap and (not right_heap or left_heap[0][0] <= right_heap[0][0]):
                # 选择左堆中的最小值
                cost, idx = heapq.heappop(left_heap)
                total_cost += cost
                # 补充新的左候选人
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                # 选择右堆中的最小值
                cost, idx = heapq.heappop(right_heap)
                total_cost += cost
                # 补充新的右候选人
                if left <= right:
                    heapq.heappush(right_heap, (costs[right], right))
                    right -= 1
        return total_cost
