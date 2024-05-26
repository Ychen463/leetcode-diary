class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0 
        if len(nums) <=1:
            return nums
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write +=1 
        for i in range(write, len(nums)):
            nums[i] = 0
        