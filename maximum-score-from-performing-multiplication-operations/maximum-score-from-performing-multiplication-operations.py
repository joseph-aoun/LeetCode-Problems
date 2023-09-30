class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = {}
        def maxi(i, j, i1):
            if i > i1 or j >= m:
                return 0
            if (i, i1, j) in dp:
                return dp[(i, i1, j)]
            ans =  max(nums[i]*multipliers[j] + maxi(i+1, j+1, i1), nums[i1]*multipliers[j] + maxi(i, j+1, i1-1))
            dp[(i, i1, j)] = ans
            return ans
        return maxi(0, 0, n-1)