# ============== Approach 1: Sort ==============
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse=True)
#         return nums[k-1]

# ============== Approach 2: Min-Heap ==============
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         min_heap = []
#         for num in nums:
#             heapq.heappush(min_heap,num)
#             if len(min_heap) > k:
#                 heapq.heappop(min_heap)
#         return min_heap[0]
# ============== Approach 3: Quickselect ==============
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            if k <= len(left):
                return quick_select(left, k)
            if len(left) + len(mid) <k:
                return quick_select(right, k-len(left)-len(mid))
            return pivot
        return quick_select(nums, k)

