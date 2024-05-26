class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write +=1
        for write in range(write, len(nums)):
            nums[write] =0