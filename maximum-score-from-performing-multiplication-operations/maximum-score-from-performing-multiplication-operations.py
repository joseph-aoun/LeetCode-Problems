class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = {}
        def maxi(i, j):
            if i > j or n-j-1+i >= m:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            ans =  max(nums[i]*multipliers[i+n-j-1] + maxi(i+1, j), nums[j]*multipliers[n-j-1+i] + maxi(i, j-1))
            dp[(i, j)] = ans
            return ans
        return maxi(0, n-1)