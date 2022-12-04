class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        L = sorted([c[x] for x in c.keys()], reverse = True)
        ans= 0
        
        for i in range(1, len(L)):
            if L[i] >= L[i-1]:
                if L[i - 1] != 0:
                    ans += L[i] - L[i-1] + 1
                    L[i] = max(0, L[i-1]-1)
                else:
                    ans += L[i]
                    L[i] = 0
        return ans