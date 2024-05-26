class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # cur_sum = sum(nums[:k])
        # max_avg = cur_sum/k

        # for i in range(k, len(nums)):
        #     cur_sum = cur_sum - nums[i - k] + nums[i]
        #     max_avg = max(max_avg, cur_sum/k)
        # return max_avg

        # 计算初始窗口和
        cur_sum = sum(nums[:k])
        max_sum = cur_sum

        # 使用滑动窗口遍历数组
        for i in range(k, len(nums)):
            # 更新当前窗口的和
            cur_sum += nums[i] - nums[i - k]
            # 更新最大和
            
            max_sum = max(max_sum, cur_sum)
        
        # 返回最大和的平均值
        return max_sum / float(k)