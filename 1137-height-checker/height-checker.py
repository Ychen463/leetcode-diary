# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         expected = sorted(heights)
#         counter = 0
#         for i in range(len(heights)):
#             if heights[i] != expected[i]:
#                 counter+=1
#         return counter

# ================ Method 1: Bubble Sort ===================
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        print(heights)
        def bubble_sort():
            n = len(sorted_heights)
            # Loop through the array for bubble sort passes.
            for i in range(n - 1):
                # Inner loop to compare and swap elements.
                for j in range(n - i - 1):
                    # Compare and swap if elements are in the wrong order.
                    if sorted_heights[j] > sorted_heights[j + 1]:
                        sorted_heights[j], sorted_heights[j + 1] = (
                            sorted_heights[j + 1],
                            sorted_heights[j],
                        )
        sorted_heights = heights[:]
        bubble_sort()
        count = 0
        for i in range(len(sorted_heights)):
            if heights[i] != sorted_heights[i]:
                count +=1
        return count
        