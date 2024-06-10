class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        prefix_sum_mod = 0
        count = 0
        for num in nums:
            prefix_sum_mod = (prefix_sum_mod + num) % k 
            if prefix_sum_mod< 0:
                prefix_sum_mod += k # 变成正数
            if prefix_sum_mod in prefix_count:
                count += prefix_count[prefix_sum_mod]
            else:
                prefix_count[prefix_sum_mod] = 0
            prefix_count[prefix_sum_mod] += 1
        return count

        