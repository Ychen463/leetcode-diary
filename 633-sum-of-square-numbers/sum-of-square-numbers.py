# ================== Approach 3: Using Sqrt Function =============
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:      
        a = 0
        # math.sqrt 返回浮点数结果。
        # math.isqrt 返回整数结果。
        b = math.isqrt(c)
        while a <= b:
            total = a*a + b*b
            if total == c:
                return True
            elif total < c:
                a +=1
            else:
                b-=1
        return False