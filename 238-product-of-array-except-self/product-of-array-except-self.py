class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # p1, p2 = 1, len(nums)-2
        # left_prd = [0]*len(nums)
        # right_prd = [0]*len(nums)
        # left_prd[0] = 1
        # right_prd[len(nums)-1] = 1
        # res = []

        # while p1 < len(nums) :
        #     left_prd[p1] = nums[p1-1]*left_prd[p1-1]
        #     right_prd[p2] = nums[p2+1]*right_prd[p2+1]
        #     p1 +=1
        #     p2 -=1
        # for i in range(len(left_prd)):
        #     res.append(left_prd[i] * right_prd[i])
        # print(res)
        # return res
        n = len(nums)
        res = [1] * n

        for i in range(1,len(nums)):
            res[i] = nums[i-1]*res[i-1]
        right_product = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = right_product * res[i]
            right_product *= nums[i]
        return res

        