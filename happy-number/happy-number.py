class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(100):
            if n == 1:
                return True
            n = sum(x*x for x in map(int, list(str(n))))
        return False