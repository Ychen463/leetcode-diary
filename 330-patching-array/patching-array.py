class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        added = 0
        i = 0
        
        while miss <= n:
            # 如果当前的数字可以覆盖miss，则更新miss
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            # 否则添加一个新的数
            else:
                miss += miss
                added += 1
                
        return added