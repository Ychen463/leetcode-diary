class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums = [1,2,3,4]
        # right_nums = [24,12,4,1]
        # left_nums = [1,1,2,6]
        
        # res = right * left

        p1, p2 = 1, len(nums)-2
        left_prd = [0]*len(nums)
        right_prd = [0]*len(nums)
        left_prd[0] = 1
        right_prd[len(nums)-1] = 1
        res = []

        while p1 < len(nums) :
            left_prd[p1] = nums[p1-1]*left_prd[p1-1]
            right_prd[p2] = nums[p2+1]*right_prd[p2+1]
            p1 +=1
            p2 -=1
        for i in range(len(left_prd)):
            res.append(left_prd[i] * right_prd[i])
        print(res)
        return res
        