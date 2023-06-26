from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        D = {1:"", 2:"abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        ans = []
        curr = []
        def solve(i = 0):
            if i == len(digits):
                if curr:
                    ans.append(''.join(curr))
                return
            for x in D[int(digits[i])]:
                curr.append(x)
                solve(i+1)
                curr.pop()
        solve()
        return ans