class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return list(accumulate(nums, xor))[-1]