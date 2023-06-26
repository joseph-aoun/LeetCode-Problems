class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        ok = 1
        for i in range(1, n+1):
            dp.append(1 + dp[i - ok])
            if i&(i-1) == 0: ok <<= 1
        return dp