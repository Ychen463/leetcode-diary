class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        p1, p2 = 0, len(nums) -1
        counter =0
        while p1 < p2:
            print(p1, nums[p1], p2, nums[p2], counter )
            if nums[p1] + nums[p2] == k:
                counter+=1
                p2 -=1
                p1 +=1
            elif nums[p1] + nums[p2] < k:
                p1+=1
            elif nums[p1] + nums[p2] > k:
                p2-=1        
        return counter
            