class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefix_sum = 0
        prefix_sum_mod = {0:-1}

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if k != 0:
                prefix_sum %= k # 余数
            if prefix_sum in prefix_sum_mod:
                if i-prefix_sum_mod[prefix_sum] >=2:
                    return True
            else:
                prefix_sum_mod[prefix_sum] = i
        return False
            
            
            

        