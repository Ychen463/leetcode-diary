# =============== Approach 1: Brute Force =============== 
class Solution:
    def check_prime(self, x): # 定义一个方法用来判断一个数是否是质数
        for i in range(2, int(x**0.5) + 1): # 如果x能够被i整除，说明x不是质数
            if x % i == 0:
                return False
        # 如果没有发现可以整除x的i，则x是质数
        return True
    
    # 主函数，用来执行质数减法操作
    def primeSubOperation(self, nums: List[int]) -> bool:
        for i in range(len(nums)): # 遍历数组中的每个元素
            if i == 0:
                bound = nums[0] # 对于第一个元素，我们需要找到一个小于nums[0]的最大质数
            else:
                # 对于其他位置的元素，我们需要找到一个质数，使得
                # 当前元素减去该质数后尽可能接近上一个元素
                bound = nums[i] - nums[i - 1]
        
            # 如果bound小于或等于0，说明无法使数组严格递增，直接返回False
            if bound <= 0:
                return False

            # 从bound - 1开始寻找小于bound的最大质数
            largest_prime = 0
            for j in range(bound - 1, 1, -1):
                # 使用check_prime函数判断j是否为质数
                if self.check_prime(j):
                    largest_prime = j
                    break
        
            nums[i] = nums[i] - largest_prime # 用找到的最大质数减去当前的nums[i]
        return True        # 如果完成整个循环，说明数组可以变成严格递增，返回True
# =============== Approach 2: Storing the primes =============== 
class Solution:
    def isprime(self, x):    # 定义一个方法来判断一个数是否是质数
        for i in range(2, isqrt(x)+1): # 遍历从2到sqrt(n)的整数，如果有因数说明n不是质数
            if x % i ==0:
                return False
        return True        # 如果没有找到任何因数，则n是质数
    def primeSubOperation(self, nums):
        maxElement = max(nums) # 找出数组中的最大元素
        prev_primes = [0] * (maxElement + 1)
        for i in range(2, maxElement + 1):
            if self.isprime(i):
                prev_primes[i] = i
            else:
                prev_primes[i] = prev_primes[i-1]
        for i in range(len(nums)): # 遍历数组中的每个元素
            if i == 0:
                bound = nums[0]
            else:
            # 对于其他元素，我们需要找到一个质数，使得当前元素减去该质数后尽可能接近上一个元素
                bound = nums[i] - nums[i - 1]
            
            # 如果bound小于等于0，说明无法使数组严格递增，直接返回False
            if bound <= 0:
                return False
            # 使用previous_prime数组找到小于bound的最大质数
            largest_prime = prev_primes[bound - 1]
            # 用找到的最大质数减去当前的nums[i]
            nums[i] -= largest_prime
        # 如果完成整个循环，说明数组可以变成严格递增，返回True
        return True