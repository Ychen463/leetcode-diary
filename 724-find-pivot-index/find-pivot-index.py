class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]  # 首先从 right_sum 中减去当前元素
            if left_sum == right_sum:  # 比较左侧和右侧的和
                return i
            left_sum += nums[i]  # 然后再将当前元素加到 left_sum 中
        return -1

        