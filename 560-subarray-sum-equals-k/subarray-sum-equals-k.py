
# # Method 1: Prefix Sum + HashMap
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_sum_count 是一个哈希表（使用 defaultdict），用于存储每个前缀和出现的次数。
        prefixSumCount = defaultdict(int)
        # 将前缀和为0的情况存入哈希表，prefix_sum_count[0] = 1，
        # 表示初始状态下前缀和为0出现一次。
        prefixSumCount[0] = 1
        currentSum = 0
        count = 0

        for num in nums:
            currentSum += num
            if currentSum - k in prefixSumCount:
                count += prefixSumCount[currentSum - k ]
            prefixSumCount[currentSum] +=1
        return count
            
# ------------------------------------------------------------
# 通过预处理数组，创建一个前缀和数组，我们可以在常数时间内计算任何区间的和。
# Method 2: Prefix Sum, Brute Force, Using Cumulative Sum

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         prefixSum = [0] * (len(nums) + 1)
#         count = 0
#         # 计算前缀和数组
#         for i in range(1, len(nums) + 1):
#             prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
#         for start in range(len(nums)):
#             for end in range(start + 1, len(nums) + 1):
#                 if prefixSum[end] - prefixSum[start] == k:
#                     count += 1
#         return count

# ------------------------------------------------------------
# Method 3: Prefix Sum, Brute Force, Without Space
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         for start in range(len(nums)):
#             sumValue = 0
#             for end in range(start,len(nums)):
#                 sumValue += nums[end]
#                 if sumValue == k:
#                     count +=1
#         return count

