# Method : Prefix_sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen_mode = {0 : -1}
        prefix_mod = 0
        for i in range(len(nums)):
            prefix_mod = (prefix_mod+nums[i]) % k
            if prefix_mod in seen_mode:
                if i - seen_mode[prefix_mod] >= 2:
                    return True
            else:
                seen_mode[prefix_mod] = i
        return False
        
            
            
            

        