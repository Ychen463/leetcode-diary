class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_count = {0:1}
        mod_sum = 0
        counter  = 0

        for i in range(len(nums)):
            mod_sum = (mod_sum + nums[i] )%k
            if mod_sum < 0:
                mod_sum += k
            if mod_sum in mod_count:
                counter += mod_count[mod_sum]
            else:
                mod_count[mod_sum] = 0
            mod_count[mod_sum]+=1
        return counter

        