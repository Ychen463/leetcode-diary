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
# import random
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def quick_select(nums, k):
#             pivot = random.choice(nums) # 随机选择一个枢轴值（pivot）作为分区基准
#             # 初始化三个列表：
#             # 1. left存放大于pivot的元素，
#             # 2. right存放小于pivot的元素，
#             # 3. mid存放等于pivot的元素
#             left, mid, right = [], [], []
                    
#             for num in nums: # 遍历nums中的每个元素，将它们分类到left, mid, 或 right列表中
#                 if num > pivot:
#                     left.append(num) # 大于pivot的元素放入left
#                 elif num < pivot:
#                     right.append(num) # 小于pivot的元素放入right
#                 else:
#                     mid.append(num) # 等于pivot的元素放入mid
#             # 检查是否第 k 大的元素位于left部分
#             if k <= len(left):
#                 return quick_select(left, k)
#             if len(left) + len(mid) <k: # 检查是否第 k 大的元素位于right部分
#                 return quick_select(right, k-len(left)-len(mid))
#             return pivot # 如果不在left或right，说明第 k 大的元素就是pivot
#         return quick_select(nums, k) # 调用quick_select函数查找第 k 大的元素

# ============== Approach 4: Counting Sort ==============

# 在使用 计数排序（Counting Sort） 方法解决第 k 大元素的问题时，假设数组中元素的值在一个已知的范围内（例如，数组中的整数范围为 [min_val, max_val]）。计数排序适用于这种情况，因为它依赖于统计每个整数出现的次数，避免了直接排序，从而达到高效查找第 k 大元素的目的。

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # 找到数组的最小值和最大值，定义计数数组的范围
        min_val, max_val = min(nums), max(nums)

        # 构建计数数组，长度为 max_val - min_val + 1
        count = [0] * (max_val - min_val + 1)
        # 填充计数数组，记录每个数字出现的次数
        for num in nums:
            count[num - min_val] += 1
        # 从计数数组的末尾（最大值）往前遍历，寻找第 k 大的元素
        for i in range(len(count) - 1, -1, -1):
            k -= count[i]
            # 当 k 减到 0 或以下时，返回对应的数值
            if k <= 0:
                return i + min_val