class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_counter = 0
        left = right = 0
        max_length = 0
        for right in range(len(nums)):

            if nums[right] == 0:
                zero_counter += 1
            while zero_counter > k:
                if nums[left] == 0:
                    zero_counter -=1
                left += 1
            max_length = max(max_length, right - left +1)
        return max_length

