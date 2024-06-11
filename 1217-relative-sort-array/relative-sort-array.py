# # ================ Approach 1: Using Hash Map for Counting and Sorting =========
# import collections
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
#         dict1 = Counter(arr1)
#         res = []
#         for num in arr2:
#             if num in dict1:
#                 for i in range(dict1[num]):
#                     res.append(num)
#         res2 = sorted([ num for num in arr1 if num not in arr2])
#         return res+ res2

# ================ Approach 2: Using Counting Sort ===========================
import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maxValue = max(arr1)
        count = [0] * (maxValue+1)
        for num in arr1:
            count[num] += 1
        res = []
        # 按照arr2的顺序，添加到res
        for num in arr2:
            while count[num] > 0:
                res.append(num)
                count[num] -= 1
        print(count)
        for num in range(maxValue +1 ):
            while count[num] > 0:
                res.append(num)
                count[num] -=1
        return res
