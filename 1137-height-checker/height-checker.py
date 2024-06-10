# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         expected = sorted(heights)
#         counter = 0
#         for i in range(len(heights)):
#             if heights[i] != expected[i]:
#                 counter+=1
#         return counter

# # ================ Method 1: Bubble Sort ===================
# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         print(heights)
#         def bubble_sort():
#             n = len(sorted_heights)
#             # Loop through the array for bubble sort passes.
#             for i in range(n - 1):
#                 # Inner loop to compare and swap elements.
#                 for j in range(n - i - 1):
#                     # Compare and swap if elements are in the wrong order.
#                     if sorted_heights[j] > sorted_heights[j + 1]:
#                         sorted_heights[j], sorted_heights[j + 1] = (
#                             sorted_heights[j + 1],
#                             sorted_heights[j],
#                         )
#         sorted_heights = heights[:]
#         bubble_sort()
#         count = 0
#         for i in range(len(sorted_heights)):
#             if heights[i] != sorted_heights[i]:
#                 count +=1
#         return count

# # ================ Method 2: Merge Sort ===================
class Solution:
    # 该函数负责将两个已排序的子数组合并成一个排序的数组
    def merge(self, arr: List[int], left: int, mid: int, right: int, tempArr: List[int]):
        start1, end1 = left, mid
        start2, end2 = mid+1, right

        tempArr[left: right+1] = arr[left: right+1]

        i, j, k = start1, start2, left
        while i <= end1 and j <= end2:
            if tempArr[i] <= tempArr[j]:
                arr[k] = tempArr[i]
                i += 1
            else:
                arr[k] = tempArr[j]
                j += 1
            k+=1
        while i <= end1:
            arr[k] = tempArr[i]
            i+=1
            k+=1
        while j <= end2:
            arr[k] = tempArr[j]
            j+=1
            k+=1

    def mergeSort(self, arr: List[int], left: int, right: int, tempArr: List[int]):
        if left >= right :
            return
        mid = left + (right-left) //2
        self.mergeSort(arr, left, mid, tempArr)
        self.mergeSort(arr, mid+1, right, tempArr)
        self.merge(arr, left, mid, right, tempArr)


    def heightChecker(self, heights: List[int]) -> int:
        tempArr = [0] * len(heights)
        sortedHeights = heights[:]

        self.mergeSort(sortedHeights, 0, len(heights)-1, tempArr)
        count = 0
        for i in range(len(heights)):
            if sortedHeights[i] != heights[i]:
                count +=1
        return count
        
