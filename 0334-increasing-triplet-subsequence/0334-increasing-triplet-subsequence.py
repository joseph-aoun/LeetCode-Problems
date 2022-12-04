class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        L = []
        
        for x in nums:
            if not L or L[-1] < x: L.append(x)
            elif L[0] >= x: L[0] = x
            else: L[1] = x
        return len(L) > 2