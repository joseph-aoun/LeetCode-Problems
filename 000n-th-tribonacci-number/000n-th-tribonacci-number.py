class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 1
        dp1 = 0
        dp2 = 1
        dp3 = 1
        
        for i in range(2, n):
            ans = dp1 + dp2 + dp3
            dp1 = dp2
            dp2 = dp3
            dp3 = ans
        
        return ans