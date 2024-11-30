import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Step 1: 将 nums1 和 nums2 按 nums2 值降序排列
        pairs = sorted(zip(nums2, nums1),reverse = True)
        
        # Step 2: 使用一个最小堆维护 nums1 的前 k 大值
        min_heap = []
        current_sum = 0
        max_score = 0

        for num2, num1 in pairs:
            heapq.heappush(min_heap, num1)
            current_sum += num1

            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)

        return max_score
            
