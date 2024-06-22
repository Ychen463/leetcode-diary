class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = [0] * (len(nums) + 1)
        count = 0
        result = 0
        odd_count[0] = 1  # 初始化，表示0个奇数的情况
        
        for num in nums:
            if num % 2 == 1:
                count += 1
            if count >= k:
                result += odd_count[count - k]
            odd_count[count] += 1
        
        return result