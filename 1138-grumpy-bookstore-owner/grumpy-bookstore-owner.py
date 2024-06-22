class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # 初始满意顾客总数
        total_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]
        
        # 找到最多可以转换为满意的顾客数
        max_extra_satisfied = 0
        current_extra_satisfied = 0
        
        # 计算第一个窗口的额外满意顾客数
        for i in range(minutes):
            if grumpy[i] == 1:
                current_extra_satisfied += customers[i]
        
        max_extra_satisfied = current_extra_satisfied
        
        # 滑动窗口
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                current_extra_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                current_extra_satisfied -= customers[i - minutes]
            max_extra_satisfied = max(max_extra_satisfied, current_extra_satisfied)
        
        # 总满意顾客数
        return total_satisfied + max_extra_satisfied