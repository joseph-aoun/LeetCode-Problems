class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = [nums2[0]]
        
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                d[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            
        ans = []
        for x in nums1:
            ans.append(d.get(x, -1))
        return ans
            