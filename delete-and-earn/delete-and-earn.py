class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        if len(set(nums)) < 2: return nums[0]*count[nums[0]]
        nums = list(set(nums))
        nums.sort()
        
        n = len(nums)
        
        dp = [0]*n
        
        dp[0] = count[nums[0]]*nums[0]
        
        dp[1] = max(dp[0], nums[1]*count[nums[1]]) if nums[1] == nums[0]+1 else dp[0] + nums[1]*count[nums[1]]
        
        for i in range(2, n):
            if nums[i] == nums[i-1] + 1:
                dp[i] = max(nums[i]*count[nums[i]] + dp[i-2], dp[i-1])
            else:
                dp[i] = dp[i-1] + nums[i]*count[nums[i]]
        
        
        return dp[-1]