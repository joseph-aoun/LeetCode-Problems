class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums.sort()
        ans = []
        last = lower
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == last:
                last += 1
            else:
                ans.append([last, nums[i]-1])
                last = nums[i] + 1
            i += 1
        if nums and nums[-1] != upper:
            ans.append([nums[-1]+1, upper])
        return ans if nums else [[lower, upper]]