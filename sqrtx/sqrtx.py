class Solution:
    def mySqrt(self, x: int) -> int:
        lb = 0
        rb = x
        while lb < rb:
            m = (lb + rb) // 2
            if m*m >= x:
                rb = m
            else:
                lb = m + 1
        return lb if lb*lb <= x else lb-1