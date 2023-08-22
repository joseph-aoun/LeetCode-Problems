class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        c, i = 0, 0
        for j in range(len(nums)):
            if nums[i] == nums[j]: c += 1
            else: c-= 1
            if c < 0:
                i = j
                c = 1
        return nums[i]