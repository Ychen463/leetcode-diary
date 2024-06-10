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

#  # ================ Method 2: Merge Sort ===================
# class Solution:
#     # 该函数负责将两个已排序的子数组合并成一个排序的数组
#     def merge(self, arr: List[int], left: int, mid: int, right: int, tempArr: List[int]):
#         start1, end1 = left, mid
#         start2, end2 = mid+1, right

#         tempArr[left: right+1] = arr[left: right+1]

#         i, j, k = start1, start2, left
#         while i <= end1 and j <= end2:
#             if tempArr[i] <= tempArr[j]:
#                 arr[k] = tempArr[i]
#                 i += 1
#             else:
#                 arr[k] = tempArr[j]
#                 j += 1
#             k+=1
#         while i <= end1:
#             arr[k] = tempArr[i]
#             i+=1
#             k+=1
#         while j <= end2:
#             arr[k] = tempArr[j]
#             j+=1
#             k+=1

#     def mergeSort(self, arr: List[int], left: int, right: int, tempArr: List[int]):
#         if left >= right :
#             return
#         mid = left + (right-left) //2
#         self.mergeSort(arr, left, mid, tempArr)
#         self.mergeSort(arr, mid+1, right, tempArr)
#         self.merge(arr, left, mid, right, tempArr)


#     def heightChecker(self, heights: List[int]) -> int:
#         tempArr = [0] * len(heights)
#         sortedHeights = heights[:]

#         self.mergeSort(sortedHeights, 0, len(heights)-1, tempArr)
#         count = 0
#         for i in range(len(heights)):
#             if sortedHeights[i] != heights[i]:
#                 count +=1
#         return count
        
# ================ Method 3: Heap Sort ===================
class Solution:
    def heapify(self, arr, n, i):
        # i 是最大节点
        largest = i
        left, right = 2*i+1, 2*i +2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if i != largest:
            arr[i], arr[largest] = arr[largest],arr[i]
            self.heapify(arr, n, largest)
    def heapSort(self, arr: List[int]):
        # 遍历数组元素，
        # 从末尾到开始，
        # 对每个元素交换根节点和最后一个元素，
        # 并对减小后的数组调用 heapify，以确保其仍为最大堆。

        # 构建最大堆
        for i in range(len(arr) // 2 - 1, -1, -1):
            self.heapify(arr, len(arr) , i)

        # 一个个地从堆中取出元素
        for i in range(len(arr) - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # 交换
            self.heapify(arr, i, 0)


    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = heights[:]
        
        # 使用堆排序对 sortedHeights 进行排序
        self.heapSort(sortedHeights)
        
        # 计算与原始数组的差异
        count = 0
        for i in range(len(heights)):
            if sortedHeights[i] != heights[i]:
                count += 1
        
        return count