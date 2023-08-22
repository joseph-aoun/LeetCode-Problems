class Solution:
    def trailingZeroes(self, n: int) -> int:
        f = t = 0
        for i in range(1, n+1):
            while i%5 == 0:
                f += 1
                i //= 5
            while i % 2 == 0:
                t += 1
                i //= 2
        return min(f, t)