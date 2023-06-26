from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        curr = []
        def valid():
            c = 0
            for x in curr:
                if x == '(':
                    c += 1
                else: c -= 1
                if c < 0: return False
            return c == 0
        def solve():
            if len(curr) > n*2:
                return 
            if len(curr) == n*2:
                if valid():
                    ans.append(''.join(curr[:]))
                return 
            curr.append('(')
            solve()
            curr.pop()
            curr.append(')')
            solve()
            curr.pop()
        solve()
        return ans