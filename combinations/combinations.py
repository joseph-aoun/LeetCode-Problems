class Solution:
    def combine(self, n: int, k: int):
        ans = []
        curr = []
        def ok(n, k, j = 1):
            if k == 0:
                ans.append(curr[:])
                return
            for i in range(j, n+1):
                curr.append(i)
                ok(n, k-1, i+1)
                curr.pop()
        ok(n, k)
        return ans