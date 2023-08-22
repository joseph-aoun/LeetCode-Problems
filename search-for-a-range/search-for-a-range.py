class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = 0
        rb = len(nums) - 1
        while lb < rb:
            m = (lb + rb) //2
            if nums[m] >= target:
                rb = m
            else:
                lb = m + 1
        ans =  [lb]
        if lb >= len(nums) or nums[lb] != target:
            return [-1, -1]
        lb = 0
        rb = len(nums) - 1
        while lb < rb:
            m = (lb + rb + 1) // 2
            if nums[m] > target:
                rb = m - 1
            else:
                lb = m
        ans.append(lb)
        return ans