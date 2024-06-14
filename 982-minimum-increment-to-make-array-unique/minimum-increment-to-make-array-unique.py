class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        countingSort = [0] * (len(nums) + max(nums)+1)
        for i in range(len(nums)):
            countingSort[nums[i]] +=1
        counter = 0 
        for i in range(len(countingSort)):
            if countingSort[i] <= 1:
                continue
            duplicates = countingSort[i] - 1
            countingSort[i + 1] += duplicates
            countingSort[i] = 1
            counter += duplicates
        return counter
        