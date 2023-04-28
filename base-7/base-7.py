class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        ok = 0
        if num < 0:
            num *=- 1
            ok = 1
        while num:
            ans += str(num%7)
            num //= 7
        ans = '-'*ok + ans[::-1]
        return ans if ans else "0"