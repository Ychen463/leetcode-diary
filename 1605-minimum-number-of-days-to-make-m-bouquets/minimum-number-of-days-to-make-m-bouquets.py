import numpy as np
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        def canMakeBouquet(days):
            flowers = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers +=1
                    if flowers == k:
                        bouquets+=1
                        flowers = 0
                else:
                    flowers = 0
                if bouquets >= m :
                    return True
            return False
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = left + (right-left) //2
            if canMakeBouquet(mid): # 判断在 mid 天内是否可以制作出 m 束花。
                right = mid 
            else:
                left = mid + 1
        # Return the minimum number of days you need 
        # to wait to be able to make m bouquets
        return left