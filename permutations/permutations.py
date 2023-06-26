from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        num = set()
        def solve():
            if len(num) == len(nums):
                ans.append(curr[:])
                return
            for x in nums:
                if x not in num:
                    curr.append(x)
                    num.add(x)
                    solve()
                    num.remove(x)
                    curr.pop()
        solve()
        return ans