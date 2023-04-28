class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = left
        for i in range(32):
            curr = (right | (1 << i))^((1 << i))
            if left <= curr <= right:
                ans |= (1 << i)
                ans ^= (1 << i)
        return ans