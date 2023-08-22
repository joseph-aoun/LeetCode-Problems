class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def backTrack(i):
            if i == len(nums):
                ans.append(curr[:])
                return
            curr.append(nums[i])
            backTrack(i+1)
            curr.pop()
            backTrack(i+1)
        backTrack(0)
        return ans
        
        return ans